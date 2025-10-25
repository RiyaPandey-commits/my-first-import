"""
Twitter/X Collector
Collects mentions, replies, and discussions about the company
"""

import tweepy
import os
from datetime import datetime, timedelta


class TwitterCollector:
    def __init__(self):
        # Twitter API v2 authentication
        self.api_key = os.getenv('TWITTER_API_KEY')
        self.api_secret = os.getenv('TWITTER_API_SECRET')
        self.access_token = os.getenv('TWITTER_ACCESS_TOKEN')
        self.access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
        self.client = None

        if all([self.api_key, self.api_secret, self.access_token, self.access_token_secret]):
            try:
                self.client = tweepy.Client(
                    consumer_key=self.api_key,
                    consumer_secret=self.api_secret,
                    access_token=self.access_token,
                    access_token_secret=self.access_token_secret
                )
            except Exception as e:
                print(f"Twitter API authentication failed: {str(e)}")

    def collect(self, company_name=None, depth='standard'):
        """
        Collect tweets mentioning the company

        Args:
            company_name: Company name or Twitter handle
            depth: Research depth (quick, standard, deep)

        Returns:
            List of tweet dictionaries
        """
        tweets_data = []

        if not self.client:
            print("Warning: Twitter API not configured")
            return tweets_data

        try:
            handle = os.getenv('COMPANY_TWITTER_HANDLE') or company_name

            if not handle:
                print("Warning: No Twitter handle provided")
                return tweets_data

            # Remove @ if present
            handle = handle.lstrip('@')

            # Determine search depth
            tweet_limits = {
                'quick': 50,
                'standard': 100,
                'deep': 300
            }
            limit = tweet_limits.get(depth, 100)

            # Search for tweets
            query = f"@{handle} OR {company_name} -is:retweet"
            tweets = self.client.search_recent_tweets(
                query=query,
                max_results=min(limit, 100),  # API limit per request
                tweet_fields=['created_at', 'public_metrics', 'author_id'],
                expansions=['author_id'],
                user_fields=['username', 'name']
            )

            if tweets.data:
                # Create user lookup
                users = {user.id: user for user in tweets.includes.get('users', [])}

                for tweet in tweets.data:
                    author = users.get(tweet.author_id)
                    tweets_data.append({
                        'id': tweet.id,
                        'text': tweet.text,
                        'created_at': tweet.created_at.isoformat(),
                        'author': author.username if author else 'Unknown',
                        'author_name': author.name if author else 'Unknown',
                        'likes': tweet.public_metrics.get('like_count', 0),
                        'retweets': tweet.public_metrics.get('retweet_count', 0),
                        'replies': tweet.public_metrics.get('reply_count', 0),
                        'platform': 'twitter',
                        'collected_at': datetime.now().isoformat()
                    })

            print(f"Collected {len(tweets_data)} tweets")

        except Exception as e:
            print(f"Error collecting Twitter data: {str(e)}")

        return tweets_data
