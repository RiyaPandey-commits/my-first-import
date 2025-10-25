"""
AI Response Generator
Generates appropriate responses to customer feedback
"""

import os
import json

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


class ResponseGenerator:
    def __init__(self):
        self.openai_key = os.getenv('OPENAI_API_KEY')
        self.anthropic_key = os.getenv('ANTHROPIC_API_KEY')
        self.company_name = os.getenv('COMPANY_NAME', 'Our Company')

        # Initialize AI client
        if OPENAI_AVAILABLE and self.openai_key:
            openai.api_key = self.openai_key
            self.provider = 'openai'
        elif ANTHROPIC_AVAILABLE and self.anthropic_key:
            self.anthropic_client = anthropic.Anthropic(api_key=self.anthropic_key)
            self.provider = 'anthropic'
        else:
            self.provider = None
            print("Warning: No AI provider configured for response generation")

    def generate_single_response(self, review_text, sentiment, platform='general'):
        """
        Generate a response to a single review or comment

        Args:
            review_text: The review or comment text
            sentiment: Sentiment classification (positive/negative/neutral)
            platform: Platform where the review was posted

        Returns:
            Generated response text
        """
        if not self.provider:
            return "Thank you for your feedback. We appreciate your input."

        # Craft appropriate prompt based on sentiment
        tone_guidance = {
            'positive': 'grateful and encouraging',
            'negative': 'empathetic, apologetic, and solution-focused',
            'neutral': 'professional and helpful'
        }

        tone = tone_guidance.get(sentiment, 'professional')

        prompt = f"""Generate a professional, {tone} response to this customer feedback on {platform}.

Customer feedback:
{review_text}

Sentiment: {sentiment}

Guidelines:
- Keep response concise (2-3 sentences)
- Be authentic and personalized
- For negative feedback: acknowledge the issue, apologize, and offer a solution
- For positive feedback: express gratitude and encourage continued engagement
- Include company name: {self.company_name}
- Match the tone to the platform ({platform})
- Do not make promises you cannot keep
- Be helpful and action-oriented

Generate the response:"""

        try:
            if self.provider == 'openai':
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": f"You are a customer service representative for {self.company_name}."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,
                    max_tokens=200
                )
                return response.choices[0].message.content.strip()

            elif self.provider == 'anthropic':
                message = self.anthropic_client.messages.create(
                    model="claude-3-5-sonnet-20241022",
                    max_tokens=200,
                    messages=[
                        {"role": "user", "content": prompt}
                    ]
                )
                return message.content[0].text.strip()

        except Exception as e:
            print(f"Error generating response: {str(e)}")
            return "Thank you for your feedback. We appreciate you taking the time to share your experience."

    def generate_responses(self, sources_data, analysis):
        """
        Generate responses for all collected feedback

        Args:
            sources_data: Dictionary of data from all sources
            analysis: Analysis results from GenAI analyzer

        Returns:
            Dictionary of generated responses
        """
        responses = {}

        for source, data in sources_data.items():
            source_responses = []
            items = data.get('data', [])

            # Generate responses for high-priority items
            # Focus on negative feedback and high-impact positive feedback
            for item in items[:20]:  # Limit to first 20 items per source
                text = item.get('review') or item.get('text') or item.get('snippet', '')

                if not text:
                    continue

                # Determine sentiment
                rating = item.get('rating', 0)
                if rating:
                    sentiment = 'positive' if rating >= 4 else 'negative' if rating <= 2 else 'neutral'
                else:
                    sentiment = 'neutral'

                # Generate response
                response = self.generate_single_response(text, sentiment, source)

                source_responses.append({
                    'original_text': text,
                    'sentiment': sentiment,
                    'generated_response': response,
                    'platform': source,
                    'item_id': item.get('id')
                })

            responses[source] = source_responses

        return responses

    def generate_executive_response(self, analysis):
        """
        Generate an executive summary response to overall perception

        Args:
            analysis: Comprehensive analysis from GenAI analyzer

        Returns:
            Executive action plan
        """
        if not self.provider:
            return "Executive response generation requires AI provider configuration."

        prompt = f"""Based on this customer perception analysis, create an executive action plan.

Analysis:
{json.dumps(analysis, indent=2)}

Create a brief executive action plan that includes:
1. Situation summary (2-3 sentences)
2. Top 3 immediate actions to take
3. Top 3 strategic initiatives
4. Communication recommendations

Keep it concise and actionable."""

        try:
            if self.provider == 'openai':
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are a business strategy consultant."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.5,
                    max_tokens=500
                )
                return response.choices[0].message.content

            elif self.provider == 'anthropic':
                message = self.anthropic_client.messages.create(
                    model="claude-3-5-sonnet-20241022",
                    max_tokens=500,
                    messages=[
                        {"role": "user", "content": prompt}
                    ]
                )
                return message.content[0].text

        except Exception as e:
            print(f"Error generating executive response: {str(e)}")
            return "Error generating executive action plan."
