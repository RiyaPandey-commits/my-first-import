"""
Google Play Store Review Collector
Collects and parses reviews from Google Play Store
"""

from google_play_scraper import app, reviews, Sort
import os
from datetime import datetime


class PlayStoreCollector:
    def __init__(self):
        self.app_id = os.getenv('GOOGLE_PLAY_APP_ID')

    def collect(self, company_name=None, depth='standard'):
        """
        Collect reviews from Google Play Store

        Args:
            company_name: Company/app package ID
            depth: Research depth (quick, standard, deep)

        Returns:
            List of review dictionaries
        """
        review_data = []

        try:
            app_id = self.app_id

            if not app_id:
                print("Warning: No app ID provided for Play Store collection")
                return review_data

            # Determine how many reviews to fetch based on depth
            review_limits = {
                'quick': 50,
                'standard': 200,
                'deep': 500
            }
            limit = review_limits.get(depth, 200)

            # Fetch reviews
            result, _ = reviews(
                app_id,
                lang='en',
                country='us',
                sort=Sort.NEWEST,
                count=limit
            )

            # Parse and structure reviews
            for review in result:
                review_data.append({
                    'id': review.get('reviewId'),
                    'title': '',
                    'review': review.get('content', ''),
                    'rating': review.get('score', 0),
                    'date': review.get('at', datetime.now()).isoformat(),
                    'user': review.get('userName', 'Anonymous'),
                    'thumbs_up': review.get('thumbsUpCount', 0),
                    'platform': 'play_store',
                    'collected_at': datetime.now().isoformat()
                })

            print(f"Collected {len(review_data)} reviews from Play Store")

        except Exception as e:
            print(f"Error collecting Play Store reviews: {str(e)}")

        return review_data
