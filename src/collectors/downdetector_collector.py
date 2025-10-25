"""
Downdetector Collector
Monitors service outage reports and user complaints
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os


class DowndetectorCollector:
    def __init__(self):
        self.base_url = "https://downdetector.com"

    def collect(self, company_name=None, depth='standard'):
        """
        Collect outage reports from Downdetector

        Args:
            company_name: Company name to search for
            depth: Research depth (quick, standard, deep)

        Returns:
            List of outage report dictionaries
        """
        reports = []

        try:
            if not company_name:
                company_name = os.getenv('COMPANY_NAME')

            if not company_name:
                print("Warning: No company name provided for Downdetector")
                return reports

            # Format company name for URL
            company_slug = company_name.lower().replace(' ', '-')
            url = f"{self.base_url}/status/{company_slug}"

            # Fetch the page
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }

            response = requests.get(url, headers=headers, timeout=10)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')

                # Parse outage information
                # Note: Downdetector's structure may change, this is a general approach

                # Get current status
                status_element = soup.find('div', class_='status')
                current_status = status_element.get_text(strip=True) if status_element else 'Unknown'

                # Get recent comments/reports
                comments = soup.find_all('div', class_='comment')

                for i, comment in enumerate(comments):
                    if depth == 'quick' and i >= 10:
                        break
                    if depth == 'standard' and i >= 30:
                        break
                    if depth == 'deep' and i >= 100:
                        break

                    text = comment.get_text(strip=True)
                    reports.append({
                        'id': f"downdetector_{i}_{datetime.now().timestamp()}",
                        'text': text,
                        'status': current_status,
                        'platform': 'downdetector',
                        'collected_at': datetime.now().isoformat()
                    })

                print(f"Collected {len(reports)} reports from Downdetector")

            else:
                print(f"Downdetector page not found for {company_name}")

        except Exception as e:
            print(f"Error collecting Downdetector data: {str(e)}")

        return reports
