# Complete Setup Guide

## Step-by-Step Setup Instructions

### 1. System Requirements

- **Python**: 3.8 or higher
- **Operating System**: Windows, macOS, or Linux
- **RAM**: Minimum 4GB (8GB recommended for deep research)
- **Disk Space**: 500MB free space
- **Internet**: Stable connection required for API calls

### 2. API Keys Setup

#### OpenAI API Key (Recommended)
1. Go to https://platform.openai.com
2. Sign up or log in
3. Navigate to API Keys section
4. Click "Create new secret key"
5. Copy the key and save it to your `.env` file

#### Anthropic API Key (Alternative)
1. Go to https://console.anthropic.com
2. Sign up or log in
3. Navigate to API Keys
4. Generate new key
5. Copy to `.env` file

#### Twitter API Setup
1. Visit https://developer.twitter.com/en/portal/dashboard
2. Click "Create Project"
3. Fill in project details
4. Create an app within the project
5. Go to "Keys and tokens" tab
6. Generate:
   - API Key and Secret
   - Access Token and Secret
7. Copy all four values to `.env`

#### Google API Setup
1. Visit https://console.cloud.google.com
2. Create a new project
3. Enable "Places API"
4. Go to Credentials
5. Create API Key
6. Copy to `.env`

### 3. Application Configuration

Edit your `.env` file with company details:

```bash
# Replace with your actual company information
COMPANY_NAME=Tesla
COMPANY_APP_NAME=Tesla
COMPANY_TWITTER_HANDLE=@Tesla

# App Store ID (find it in your App Store URL)
# Example: https://apps.apple.com/app/id123456789
APPLE_APP_ID=123456789

# Play Store package name (find it in Play Store URL)
# Example: https://play.google.com/store/apps/details?id=com.tesla.app
GOOGLE_PLAY_APP_ID=com.tesla.app
```

### 4. Testing Your Setup

Test each component:

#### Test Database
```bash
python -c "from src.database.db_manager import DatabaseManager; db = DatabaseManager(); db.initialize(); print('Database OK')"
```

#### Test Sentiment Analysis
```bash
python -c "from src.analysis.sentiment_analyzer import SentimentAnalyzer; sa = SentimentAnalyzer(); print(sa.analyze('Great product!'))"
```

#### Test AI Provider
```bash
python -c "from src.analysis.genai_analyzer import GenAIAnalyzer; ga = GenAIAnalyzer(); print('Provider:', ga.provider)"
```

### 5. Running the Application

#### Development Mode
```bash
python app.py
```

#### Production Mode
```bash
# Set production environment variables
export FLASK_DEBUG=False
export FLASK_PORT=8080

# Run with gunicorn (install first: pip install gunicorn)
gunicorn -w 4 -b 0.0.0.0:8080 app:app
```

### 6. First Research Run

1. Open browser to `http://localhost:5000`
2. Enter company name
3. Select "Quick" for first test
4. Click "Start Research"
5. Wait 30-60 seconds for results

### 7. Interpreting Results

#### Sentiment Score
- 75-100%: Excellent customer perception
- 50-74%: Good, with room for improvement
- 25-49%: Needs attention
- 0-24%: Critical issues require immediate action

#### Risk Levels
- **Low**: No significant issues detected
- **Medium**: Some concerns, monitor closely
- **High**: Multiple issues, action recommended
- **Critical**: Immediate intervention required

### 8. Common Issues and Solutions

#### Issue: "No AI provider configured"
**Solution**: Add OPENAI_API_KEY or ANTHROPIC_API_KEY to `.env`

#### Issue: "Twitter authentication failed"
**Solution**: Verify all four Twitter credentials in `.env`

#### Issue: "No reviews found"
**Solution**:
- Check company name spelling
- Verify app IDs are correct
- Some platforms may have no reviews yet

#### Issue: "Database locked"
**Solution**:
```bash
rm perception_data.db
python -c "from src.database.db_manager import DatabaseManager; DatabaseManager().initialize()"
```

#### Issue: "Module not found"
**Solution**:
```bash
pip install -r requirements.txt --upgrade
```

### 9. Optimization Tips

#### For Faster Results
- Use "Quick" research depth
- Limit to specific platforms
- Use local caching

#### For Better Accuracy
- Use "Deep" research depth
- Enable all platforms
- Run during peak hours for more data

#### For Cost Optimization
- Use Anthropic Claude (more cost-effective)
- Batch requests when possible
- Set appropriate depth levels

### 10. Scheduling Automated Research

#### Using Cron (Linux/Mac)
```bash
# Edit crontab
crontab -e

# Add daily research at 9 AM
0 9 * * * cd /path/to/app && python -c "from app import *; start_automated_research()"
```

#### Using Task Scheduler (Windows)
1. Open Task Scheduler
2. Create Basic Task
3. Set trigger (e.g., daily at 9 AM)
4. Action: Start a program
5. Program: `python`
6. Arguments: `app.py --automated`

### 11. Security Checklist

- [ ] `.env` file is in `.gitignore`
- [ ] API keys are valid and not shared
- [ ] Database has proper permissions
- [ ] Application runs on internal network only (for development)
- [ ] SSL/TLS enabled for production
- [ ] Rate limiting configured
- [ ] Error messages don't expose sensitive info

### 12. Backup and Maintenance

#### Backup Database
```bash
cp perception_data.db perception_data_backup_$(date +%Y%m%d).db
```

#### Clear Old Data
```bash
python -c "from src.database.db_manager import DatabaseManager; db = DatabaseManager(); db.cleanup_old_data(days=90)"
```

#### Update Dependencies
```bash
pip install -r requirements.txt --upgrade
```

### 13. Scaling for Production

#### Use Production Database
```bash
# PostgreSQL example
DATABASE_URL=postgresql://user:password@localhost/perception_db
```

#### Deploy with Docker
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

#### Environment-Specific Configs
- Development: SQLite, debug=True
- Staging: PostgreSQL, limited data
- Production: PostgreSQL, full monitoring

### 14. Monitoring and Alerts

Set up monitoring for:
- API rate limits
- Database size
- Response times
- Error rates
- Cost tracking

### 15. Getting Help

If you encounter issues:
1. Check this guide
2. Review error logs
3. Test individual components
4. Check API provider status pages
5. Review API documentation
6. Open GitHub issue with details

---

## Quick Reference Commands

```bash
# Start app
python app.py

# Initialize database
python -c "from src.database.db_manager import DatabaseManager; DatabaseManager().initialize()"

# Test configuration
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('Company:', os.getenv('COMPANY_NAME'))"

# Check dependencies
pip list

# Update all dependencies
pip install -r requirements.txt --upgrade

# Run tests (if you add them)
python -m pytest tests/
```

Your app is now ready to provide deep insights into customer perception!
