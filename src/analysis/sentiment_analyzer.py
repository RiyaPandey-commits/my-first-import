"""
Sentiment Analysis Module
Analyzes sentiment using multiple approaches for accuracy
"""

from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import numpy as np


class SentimentAnalyzer:
    def __init__(self):
        self.vader = SentimentIntensityAnalyzer()

    def analyze(self, text):
        """
        Analyze sentiment of text using multiple methods

        Args:
            text: Text to analyze

        Returns:
            Dictionary with sentiment scores and classification
        """
        if not text or len(text.strip()) == 0:
            return {
                'polarity': 0,
                'subjectivity': 0,
                'vader_compound': 0,
                'classification': 'neutral',
                'confidence': 0
            }

        # TextBlob sentiment
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        # VADER sentiment
        vader_scores = self.vader.polarity_scores(text)
        vader_compound = vader_scores['compound']

        # Combined classification
        # Average the polarity and vader compound score
        combined_score = (polarity + vader_compound) / 2

        # Classify sentiment
        if combined_score >= 0.3:
            classification = 'positive'
        elif combined_score <= -0.3:
            classification = 'negative'
        else:
            classification = 'neutral'

        # Calculate confidence based on agreement between methods
        confidence = 1 - abs(polarity - vader_compound) / 2

        return {
            'polarity': float(polarity),
            'subjectivity': float(subjectivity),
            'vader_compound': float(vader_compound),
            'vader_positive': float(vader_scores['pos']),
            'vader_negative': float(vader_scores['neg']),
            'vader_neutral': float(vader_scores['neu']),
            'combined_score': float(combined_score),
            'classification': classification,
            'confidence': float(confidence)
        }

    def analyze_batch(self, texts):
        """
        Analyze sentiment for a batch of texts

        Args:
            texts: List of texts to analyze

        Returns:
            List of sentiment dictionaries
        """
        return [self.analyze(text) for text in texts]

    def get_aggregate_sentiment(self, sentiments):
        """
        Get aggregate sentiment statistics from multiple sentiment analyses

        Args:
            sentiments: List of sentiment dictionaries

        Returns:
            Aggregate statistics
        """
        if not sentiments:
            return {
                'total_count': 0,
                'positive_count': 0,
                'negative_count': 0,
                'neutral_count': 0,
                'average_polarity': 0,
                'average_subjectivity': 0
            }

        positive_count = sum(1 for s in sentiments if s['classification'] == 'positive')
        negative_count = sum(1 for s in sentiments if s['classification'] == 'negative')
        neutral_count = sum(1 for s in sentiments if s['classification'] == 'neutral')

        polarities = [s['polarity'] for s in sentiments if 'polarity' in s]
        subjectivities = [s['subjectivity'] for s in sentiments if 'subjectivity' in s]

        return {
            'total_count': len(sentiments),
            'positive_count': positive_count,
            'negative_count': negative_count,
            'neutral_count': neutral_count,
            'positive_percentage': (positive_count / len(sentiments)) * 100 if sentiments else 0,
            'negative_percentage': (negative_count / len(sentiments)) * 100 if sentiments else 0,
            'neutral_percentage': (neutral_count / len(sentiments)) * 100 if sentiments else 0,
            'average_polarity': float(np.mean(polarities)) if polarities else 0,
            'average_subjectivity': float(np.mean(subjectivities)) if subjectivities else 0
        }
