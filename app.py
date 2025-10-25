"""
Company Perception Research Application
Main Flask application for analyzing customer perceptions across multiple platforms
"""

from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import os
from datetime import datetime

# Import data collectors
from src.collectors.app_store_collector import AppStoreCollector
from src.collectors.play_store_collector import PlayStoreCollector
from src.collectors.twitter_collector import TwitterCollector
from src.collectors.google_reviews_collector import GoogleReviewsCollector
from src.collectors.downdetector_collector import DowndetectorCollector
from src.collectors.web_collector import WebCollector

# Import analysis engine
from src.analysis.sentiment_analyzer import SentimentAnalyzer
from src.analysis.genai_analyzer import GenAIAnalyzer
from src.analysis.response_generator import ResponseGenerator

# Import database
from src.database.db_manager import DatabaseManager

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize components
db_manager = DatabaseManager()
sentiment_analyzer = SentimentAnalyzer()
genai_analyzer = GenAIAnalyzer()
response_generator = ResponseGenerator()

# Initialize collectors
collectors = {
    'app_store': AppStoreCollector(),
    'play_store': PlayStoreCollector(),
    'twitter': TwitterCollector(),
    'google_reviews': GoogleReviewsCollector(),
    'downdetector': DowndetectorCollector(),
    'web': WebCollector()
}


@app.route('/')
def index():
    """Main dashboard page"""
    return render_template('dashboard.html')


@app.route('/api/research', methods=['POST'])
def start_research():
    """
    Start comprehensive research across all platforms
    """
    try:
        data = request.json
        company_name = data.get('company_name', os.getenv('COMPANY_NAME'))
        depth = data.get('depth', os.getenv('RESEARCH_DEPTH', 'standard'))

        results = {
            'timestamp': datetime.now().isoformat(),
            'company': company_name,
            'depth': depth,
            'sources': {}
        }

        # Collect data from all sources
        for source_name, collector in collectors.items():
            print(f"Collecting data from {source_name}...")
            source_data = collector.collect(company_name, depth=depth)
            results['sources'][source_name] = {
                'count': len(source_data),
                'data': source_data
            }

            # Store in database
            db_manager.save_reviews(source_name, source_data)

        # Perform AI analysis
        print("Analyzing with GenAI...")
        analysis = genai_analyzer.analyze_all(results['sources'])
        results['analysis'] = analysis

        # Generate responses
        print("Generating responses...")
        responses = response_generator.generate_responses(results['sources'], analysis)
        results['responses'] = responses

        # Save analysis results
        db_manager.save_analysis(results)

        return jsonify({
            'success': True,
            'results': results
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/dashboard-data')
def get_dashboard_data():
    """
    Get aggregated data for dashboard
    """
    try:
        stats = db_manager.get_statistics()
        recent_reviews = db_manager.get_recent_reviews(limit=50)
        sentiment_trends = db_manager.get_sentiment_trends()

        return jsonify({
            'success': True,
            'stats': stats,
            'recent_reviews': recent_reviews,
            'sentiment_trends': sentiment_trends
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/sources/<source_name>')
def get_source_data(source_name):
    """
    Get data from specific source
    """
    try:
        data = db_manager.get_reviews_by_source(source_name)
        return jsonify({
            'success': True,
            'source': source_name,
            'data': data
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/analyze-text', methods=['POST'])
def analyze_text():
    """
    Analyze a specific piece of text
    """
    try:
        data = request.json
        text = data.get('text', '')

        sentiment = sentiment_analyzer.analyze(text)
        ai_insights = genai_analyzer.analyze_single(text)

        return jsonify({
            'success': True,
            'sentiment': sentiment,
            'insights': ai_insights
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/generate-response', methods=['POST'])
def generate_response():
    """
    Generate AI response to a review/comment
    """
    try:
        data = request.json
        review_text = data.get('review_text', '')
        sentiment = data.get('sentiment', '')
        platform = data.get('platform', '')

        response = response_generator.generate_single_response(
            review_text,
            sentiment,
            platform
        )

        return jsonify({
            'success': True,
            'response': response
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


if __name__ == '__main__':
    # Initialize database
    db_manager.initialize()

    # Run Flask app
    port = int(os.getenv('FLASK_PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'True') == 'True'

    print(f"""
    ╔════════════════════════════════════════════════════════════╗
    ║  Company Perception Research App                          ║
    ║  Analyzing customer perceptions with AI                   ║
    ╚════════════════════════════════════════════════════════════╝

    Dashboard: http://localhost:{port}
    API Docs: http://localhost:{port}/api/
    """)

    app.run(host='0.0.0.0', port=port, debug=debug)
