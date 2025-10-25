"""
Apple App Store Review Collector
Collects and parses reviews from Apple App Store
"""

from app_store_scraper import AppStore
import os
from datetime import datetime


class AppStoreCollector:
    def __init__(self):
        self.app_name = os.getenv('COMPANY_APP_NAME')
        self.app_id = os.getenv('APPLE_APP_ID')

    def collect(self, company_name=None, depth='standard'):
        """
        Collect reviews from Apple App Store

        Args:
            company_name: Company/app name to search for
            depth: Research depth (quick, standard, deep)

        Returns:
            List of review dictionaries
        """
        reviews = []

        try:
            app_name = company_name or self.app_name

            if not app_name:
                print("Warning: No app name provided for App Store collection")
                return reviews

            # Determine how many reviews to fetch based on depth
            review_limits = {
                'quick': 50,
                'standard': 200,
                'deep': 500
            }
            limit = review_limits.get(depth, 200)

            # Fetch reviews using app-store-scraper
            app = AppStore(country='us', app_name=app_name)
            app.review(how_many=limit)

            # Parse and structure reviews
            for review in app.reviews:
                reviews.append({
                    'id': review.get('id'),
                    'title': review.get('title', ''),
                    'review': review.get('review', ''),
                    'rating': review.get('rating', 0),
                    'date': review.get('date', datetime.now()).isoformat(),
                    'user': review.get('userName', 'Anonymous'),
                    'version': review.get('version', ''),
                    'platform': 'app_store',
                    'collected_at': datetime.now().isoformat()
                })

            print(f"Collected {len(reviews)} reviews from App Store")

        except Exception as e:
            print(f"Error collecting App Store reviews: {str(e)}")

        return reviews
