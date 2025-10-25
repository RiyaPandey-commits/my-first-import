# Company Perception Research App

A comprehensive AI-powered application that researches your company's reputation and analyzes customer perceptions across multiple platforms including App Store, Play Store, Twitter, Google Reviews, Downdetector, and general web searches.

## Features

### Multi-Platform Data Collection
- **Apple App Store**: Collect and analyze iOS app reviews
- **Google Play Store**: Gather Android app reviews and ratings
- **Twitter/X**: Monitor mentions, replies, and discussions
- **Google Reviews**: Analyze Google My Business reviews
- **Downdetector**: Track service outage reports and complaints
- **Web Search**: Comprehensive web mentions and discussions

### AI-Powered Analysis
- **Sentiment Analysis**: Advanced multi-model sentiment detection using TextBlob and VADER
- **GenAI Deep Analysis**: Leverages OpenAI GPT-4 or Anthropic Claude for comprehensive insights
- **Automated Response Generation**: AI-generated contextual responses to customer feedback
- **Trend Detection**: Identify patterns and emerging themes in customer perception
- **Risk Assessment**: Automatic evaluation of reputation risks

### Interactive Dashboard
- Real-time visualization of customer sentiment
- Platform-by-platform breakdown
- Critical issues identification
- AI-generated recommendations
- Executive summaries and action plans

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- API keys for data sources (optional but recommended)

### Setup Instructions

1. **Clone the repository**
```bash
git clone <repository-url>
cd Spoon-Knife
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure environment variables**
```bash
cp .env.example .env
```

Edit `.env` file with your configuration:
```bash
# Company Information
COMPANY_NAME=YourCompanyName
COMPANY_APP_NAME=YourAppName
COMPANY_TWITTER_HANDLE=@yourcompany

# AI Provider (choose one or both)
OPENAI_API_KEY=your_openai_key_here
ANTHROPIC_API_KEY=your_anthropic_key_here

# Social Media APIs
TWITTER_API_KEY=your_twitter_api_key
TWITTER_API_SECRET=your_twitter_api_secret
TWITTER_ACCESS_TOKEN=your_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret

# App Store IDs
APPLE_APP_ID=your_app_store_id
GOOGLE_PLAY_APP_ID=com.yourcompany.app

# Google API (for reviews)
GOOGLE_API_KEY=your_google_api_key
```

4. **Initialize the database**
```bash
python -c "from src.database.db_manager import DatabaseManager; db = DatabaseManager(); db.initialize()"
```

5. **Run the application**
```bash
python app.py
```

6. **Access the dashboard**
Open your browser to: `http://localhost:5000`

## Usage

### Quick Start

1. Open the dashboard in your browser
2. Enter your company name
3. Select research depth:
   - **Quick**: Fast overview (~50 items per source)
   - **Standard**: Balanced analysis (~200 items per source)
   - **Deep**: Comprehensive research (~500 items per source)
4. Click "Start Research"
5. View AI-generated insights, sentiment analysis, and recommended responses

### API Endpoints

The application provides a REST API for programmatic access:

#### Start Research
```bash
POST /api/research
Content-Type: application/json

{
  "company_name": "YourCompany",
  "depth": "standard"
}
```

#### Get Dashboard Data
```bash
GET /api/dashboard-data
```

#### Analyze Text
```bash
POST /api/analyze-text
Content-Type: application/json

{
  "text": "Customer feedback text here"
}
```

#### Generate Response
```bash
POST /api/generate-response
Content-Type: application/json

{
  "review_text": "Customer review",
  "sentiment": "negative",
  "platform": "app_store"
}
```

## Architecture

```
Company Perception Research App
│
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── .env                        # Configuration (create from .env.example)
│
├── src/
│   ├── collectors/            # Data collection modules
│   │   ├── app_store_collector.py
│   │   ├── play_store_collector.py
│   │   ├── twitter_collector.py
│   │   ├── google_reviews_collector.py
│   │   ├── downdetector_collector.py
│   │   └── web_collector.py
│   │
│   ├── analysis/              # AI analysis modules
│   │   ├── sentiment_analyzer.py
│   │   ├── genai_analyzer.py
│   │   └── response_generator.py
│   │
│   └── database/              # Data persistence
│       └── db_manager.py
│
├── templates/                  # HTML templates
│   └── dashboard.html
│
└── static/                     # Static assets
    ├── css/
    │   └── dashboard.css
    └── js/
        └── dashboard.js
```

## AI Providers

The application supports multiple AI providers:

### OpenAI (GPT-4)
- Requires: `OPENAI_API_KEY`
- Models: GPT-4 for deep analysis
- Best for: Comprehensive analysis and nuanced understanding

### Anthropic (Claude)
- Requires: `ANTHROPIC_API_KEY`
- Models: Claude 3.5 Sonnet
- Best for: Fast, accurate analysis with strong reasoning

## Data Sources Configuration

### Twitter API
1. Create a Twitter Developer account at https://developer.twitter.com
2. Create a new project and app
3. Generate API keys and access tokens
4. Add credentials to `.env` file

### App Store & Play Store
- App Store: Use your app's Apple ID
- Play Store: Use your app's package name (e.g., com.company.app)

### Google Reviews
1. Enable Google Places API in Google Cloud Console
2. Create API key
3. Add to `.env` file

## Features in Detail

### Sentiment Analysis
Uses dual-model approach:
- **TextBlob**: Polarity and subjectivity analysis
- **VADER**: Social media-optimized sentiment detection
- Combined scoring for higher accuracy

### Deep Research Mode
When enabled, the app:
1. Collects maximum data from all sources
2. Performs comprehensive AI analysis
3. Identifies subtle trends and patterns
4. Generates detailed executive reports
5. Creates prioritized action plans

### Response Generation
AI automatically generates:
- Platform-appropriate responses
- Tone-matched replies (empathetic for negative, grateful for positive)
- Actionable solutions for complaints
- Personalized engagement messages

## Best Practices

1. **API Rate Limits**: Be mindful of API rate limits, especially with free tiers
2. **Research Frequency**: Run deep research weekly, quick checks daily
3. **Response Review**: Always review AI-generated responses before posting
4. **Data Privacy**: Ensure compliance with data protection regulations
5. **API Keys**: Never commit API keys to version control

## Troubleshooting

### No data collected
- Check API credentials in `.env`
- Verify company name and app IDs are correct
- Check internet connection and API service status

### AI analysis not working
- Ensure AI provider API key is set
- Check API quota and billing status
- Verify API key has necessary permissions

### Database errors
- Run database initialization: `python -c "from src.database.db_manager import DatabaseManager; db = DatabaseManager(); db.initialize()"`
- Check write permissions in application directory

## Security Notes

- Store API keys securely in `.env` file
- Never commit `.env` to version control
- Use environment variables in production
- Implement rate limiting for production deployment
- Review and sanitize user inputs

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For issues, questions, or contributions:
- Open an issue on GitHub
- Check existing documentation
- Review API provider documentation

## Future Enhancements

Planned features:
- Reddit integration
- LinkedIn monitoring
- Facebook reviews
- Automated reporting emails
- Slack/Teams notifications
- Multi-language support
- Historical trend analysis
- Competitor comparison
- Custom alert thresholds

---

Built with AI-powered analysis to help you understand and improve customer perception.
