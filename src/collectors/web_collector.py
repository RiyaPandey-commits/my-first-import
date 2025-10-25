"""
Web Collector
Searches the web for company mentions, reviews, and discussions
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os
import re


class WebCollector:
    def __init__(self):
        self.search_engines = {
            'google': 'https://www.google.com/search',
            'bing': 'https://www.bing.com/search'
        }

    def collect(self, company_name=None, depth='standard'):
        """
        Collect web mentions and reviews

        Args:
            company_name: Company name to search for
            depth: Research depth (quick, standard, deep)

        Returns:
            List of web mention dictionaries
        """
        mentions = []

        try:
            if not company_name:
                company_name = os.getenv('COMPANY_NAME')

            if not company_name:
                print("Warning: No company name provided for web search")
                return mentions

            # Search queries to try
            search_queries = [
                f"{company_name} reviews",
                f"{company_name} customer feedback",
                f"{company_name} complaints",
                f"{company_name} ratings"
            ]

            if depth == 'quick':
                search_queries = search_queries[:1]
            elif depth == 'deep':
                search_queries.extend([
                    f"{company_name} user experience",
                    f"{company_name} testimonials",
                    f"is {company_name} good"
                ])

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }

            for query in search_queries:
                try:
                    # Use Google search
                    params = {'q': query}
                    response = requests.get(
                        self.search_engines['google'],
                        params=params,
                        headers=headers,
                        timeout=10
                    )

                    if response.status_code == 200:
                        soup = BeautifulSoup(response.content, 'html.parser')

                        # Extract search result snippets
                        results = soup.find_all('div', class_='g')

                        for i, result in enumerate(results[:10]):  # Top 10 results per query
                            title_elem = result.find('h3')
                            snippet_elem = result.find('div', class_=['VwiC3b', 'yXK7lf'])
                            link_elem = result.find('a')

                            if title_elem and snippet_elem:
                                mentions.append({
                                    'id': f"web_{hash(query)}_{i}",
                                    'query': query,
                                    'title': title_elem.get_text(strip=True),
                                    'snippet': snippet_elem.get_text(strip=True),
                                    'url': link_elem['href'] if link_elem else '',
                                    'platform': 'web_search',
                                    'collected_at': datetime.now().isoformat()
                                })

                except Exception as e:
                    print(f"Error searching for '{query}': {str(e)}")
                    continue

            print(f"Collected {len(mentions)} web mentions")

        except Exception as e:
            print(f"Error collecting web data: {str(e)}")

        return mentions
