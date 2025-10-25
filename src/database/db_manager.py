"""
Database Manager
Manages storage and retrieval of perception data
"""

from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Text, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
import os
import json

Base = declarative_base()


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    external_id = Column(String(255))
    platform = Column(String(50))
    title = Column(String(500))
    text = Column(Text)
    rating = Column(Float)
    author = Column(String(255))
    date = Column(DateTime)
    sentiment_score = Column(Float)
    sentiment_classification = Column(String(20))
    collected_at = Column(DateTime, default=datetime.now)
    metadata = Column(JSON)


class Analysis(Base):
    __tablename__ = 'analyses'

    id = Column(Integer, primary_key=True)
    analysis_type = Column(String(50))
    results = Column(JSON)
    created_at = Column(DateTime, default=datetime.now)
    company_name = Column(String(255))


class DatabaseManager:
    def __init__(self):
        db_url = os.getenv('DATABASE_URL', 'sqlite:///perception_data.db')
        self.engine = create_engine(db_url)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def initialize(self):
        """Create all tables"""
        Base.metadata.create_all(self.engine)
        print("Database initialized successfully")

    def save_reviews(self, platform, reviews):
        """
        Save reviews to database

        Args:
            platform: Source platform name
            reviews: List of review dictionaries
        """
        try:
            for review_data in reviews:
                review = Review(
                    external_id=str(review_data.get('id')),
                    platform=platform,
                    title=review_data.get('title', ''),
                    text=review_data.get('review') or review_data.get('text') or review_data.get('snippet', ''),
                    rating=review_data.get('rating', 0),
                    author=review_data.get('user') or review_data.get('author', 'Anonymous'),
                    date=datetime.fromisoformat(review_data.get('date', datetime.now().isoformat()).replace('Z', '+00:00')) if review_data.get('date') else datetime.now(),
                    metadata=review_data
                )
                self.session.add(review)

            self.session.commit()
            print(f"Saved {len(reviews)} reviews from {platform}")

        except Exception as e:
            self.session.rollback()
            print(f"Error saving reviews: {str(e)}")

    def save_analysis(self, analysis_results):
        """
        Save analysis results

        Args:
            analysis_results: Analysis dictionary
        """
        try:
            analysis = Analysis(
                analysis_type='comprehensive',
                results=analysis_results,
                company_name=analysis_results.get('company', '')
            )
            self.session.add(analysis)
            self.session.commit()
            print("Analysis saved successfully")

        except Exception as e:
            self.session.rollback()
            print(f"Error saving analysis: {str(e)}")

    def get_reviews_by_source(self, platform, limit=100):
        """Get reviews from specific platform"""
        reviews = self.session.query(Review).filter(
            Review.platform == platform
        ).order_by(Review.date.desc()).limit(limit).all()

        return [{
            'id': r.external_id,
            'platform': r.platform,
            'title': r.title,
            'text': r.text,
            'rating': r.rating,
            'author': r.author,
            'date': r.date.isoformat() if r.date else None,
            'sentiment': r.sentiment_classification
        } for r in reviews]

    def get_recent_reviews(self, limit=50):
        """Get most recent reviews across all platforms"""
        reviews = self.session.query(Review).order_by(
            Review.date.desc()
        ).limit(limit).all()

        return [{
            'id': r.external_id,
            'platform': r.platform,
            'title': r.title,
            'text': r.text,
            'rating': r.rating,
            'author': r.author,
            'date': r.date.isoformat() if r.date else None,
            'sentiment': r.sentiment_classification
        } for r in reviews]

    def get_statistics(self):
        """Get aggregate statistics"""
        total_reviews = self.session.query(Review).count()

        # Count by platform
        platforms = {}
        for platform in ['app_store', 'play_store', 'twitter', 'google_reviews', 'downdetector', 'web_search']:
            count = self.session.query(Review).filter(Review.platform == platform).count()
            platforms[platform] = count

        # Recent stats (last 7 days)
        week_ago = datetime.now() - timedelta(days=7)
        recent_count = self.session.query(Review).filter(
            Review.collected_at >= week_ago
        ).count()

        return {
            'total_reviews': total_reviews,
            'platforms': platforms,
            'recent_count': recent_count,
            'last_updated': datetime.now().isoformat()
        }

    def get_sentiment_trends(self, days=30):
        """Get sentiment trends over time"""
        start_date = datetime.now() - timedelta(days=days)

        reviews = self.session.query(Review).filter(
            Review.date >= start_date
        ).order_by(Review.date).all()

        # Group by day
        trends = {}
        for review in reviews:
            if review.date:
                date_key = review.date.strftime('%Y-%m-%d')
                if date_key not in trends:
                    trends[date_key] = {
                        'positive': 0,
                        'negative': 0,
                        'neutral': 0,
                        'total': 0
                    }

                sentiment = review.sentiment_classification or 'neutral'
                trends[date_key][sentiment] += 1
                trends[date_key]['total'] += 1

        return trends
