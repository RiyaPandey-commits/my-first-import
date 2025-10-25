"""
GenAI Deep Analysis Module
Uses advanced AI models for deep perception analysis
"""

import os
from datetime import datetime
import json

# Support for multiple AI providers
try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

try:
    import anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False


class GenAIAnalyzer:
    def __init__(self):
        self.openai_key = os.getenv('OPENAI_API_KEY')
        self.anthropic_key = os.getenv('ANTHROPIC_API_KEY')

        # Initialize clients
        if OPENAI_AVAILABLE and self.openai_key:
            openai.api_key = self.openai_key
            self.provider = 'openai'
        elif ANTHROPIC_AVAILABLE and self.anthropic_key:
            self.anthropic_client = anthropic.Anthropic(api_key=self.anthropic_key)
            self.provider = 'anthropic'
        else:
            self.provider = None
            print("Warning: No AI provider configured. Set OPENAI_API_KEY or ANTHROPIC_API_KEY")

    def analyze_single(self, text):
        """
        Deep analysis of a single piece of text

        Args:
            text: Text to analyze

        Returns:
            Dictionary with AI insights
        """
        if not self.provider:
            return {
                'summary': 'AI provider not configured',
                'key_points': [],
                'sentiment': 'unknown',
                'topics': [],
                'urgency': 'low'
            }

        prompt = f"""Analyze the following customer feedback and provide:
1. A brief summary
2. Key points or concerns
3. Overall sentiment (positive/negative/neutral/mixed)
4. Main topics discussed
5. Urgency level (low/medium/high/critical)
6. Suggested response approach

Customer feedback:
{text}

Provide response in JSON format with keys: summary, key_points, sentiment, topics, urgency, response_approach"""

        try:
            if self.provider == 'openai':
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are an expert customer feedback analyzer."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.3
                )
                result = response.choices[0].message.content

            elif self.provider == 'anthropic':
                message = self.anthropic_client.messages.create(
                    model="claude-3-5-sonnet-20241022",
                    max_tokens=1024,
                    messages=[
                        {"role": "user", "content": prompt}
                    ]
                )
                result = message.content[0].text

            # Parse JSON response
            try:
                insights = json.loads(result)
            except:
                # If not valid JSON, create structured response
                insights = {
                    'summary': result[:200],
                    'key_points': [],
                    'sentiment': 'unknown',
                    'topics': [],
                    'urgency': 'low',
                    'response_approach': result
                }

            return insights

        except Exception as e:
            print(f"Error in AI analysis: {str(e)}")
            return {
                'summary': 'Error analyzing text',
                'error': str(e)
            }

    def analyze_all(self, sources_data):
        """
        Comprehensive analysis across all data sources

        Args:
            sources_data: Dictionary of data from all sources

        Returns:
            Comprehensive analysis report
        """
        if not self.provider:
            return {
                'overall_sentiment': 'unknown',
                'key_insights': ['AI provider not configured'],
                'recommendations': []
            }

        # Prepare summary of all data
        summary_text = "Company Perception Analysis Summary:\n\n"

        for source, data in sources_data.items():
            count = data.get('count', 0)
            summary_text += f"{source}: {count} items\n"

            # Sample a few items from each source
            items = data.get('data', [])
            if items:
                summary_text += f"Sample from {source}:\n"
                for item in items[:3]:  # First 3 items
                    text = item.get('review') or item.get('text') or item.get('snippet', '')
                    if text:
                        summary_text += f"- {text[:200]}\n"
                summary_text += "\n"

        prompt = f"""Analyze this comprehensive customer perception data and provide:

1. Overall sentiment trend (positive/negative/neutral/mixed)
2. Top 5 key insights about customer perception
3. Critical issues that need immediate attention
4. Positive aspects customers appreciate
5. Recommendations for improvement
6. Emerging themes or patterns
7. Risk assessment (low/medium/high)

{summary_text}

Provide a detailed analysis in JSON format with keys: overall_sentiment, key_insights, critical_issues, positive_aspects, recommendations, themes, risk_level, executive_summary"""

        try:
            if self.provider == 'openai':
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are an expert business analyst specializing in customer perception and brand reputation."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.3,
                    max_tokens=2000
                )
                result = response.choices[0].message.content

            elif self.provider == 'anthropic':
                message = self.anthropic_client.messages.create(
                    model="claude-3-5-sonnet-20241022",
                    max_tokens=2000,
                    messages=[
                        {"role": "user", "content": prompt}
                    ]
                )
                result = message.content[0].text

            # Parse JSON response
            try:
                analysis = json.loads(result)
            except:
                analysis = {
                    'overall_sentiment': 'mixed',
                    'key_insights': [result],
                    'critical_issues': [],
                    'positive_aspects': [],
                    'recommendations': [],
                    'themes': [],
                    'risk_level': 'medium',
                    'executive_summary': result[:500]
                }

            analysis['generated_at'] = datetime.now().isoformat()
            analysis['provider'] = self.provider

            return analysis

        except Exception as e:
            print(f"Error in comprehensive AI analysis: {str(e)}")
            return {
                'overall_sentiment': 'unknown',
                'error': str(e),
                'key_insights': ['Error performing analysis'],
                'recommendations': ['Check AI provider configuration']
            }
