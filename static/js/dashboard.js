// Dashboard JavaScript

let sentimentChart = null;
let platformChart = null;

// Initialize
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('start-research').addEventListener('click', startResearch);
    loadDashboardData();
});

async function startResearch() {
    const companyName = document.getElementById('company-name').value;
    const depth = document.getElementById('research-depth').value;

    if (!companyName) {
        alert('Please enter a company name');
        return;
    }

    // Show loading
    document.getElementById('loading').style.display = 'block';
    document.getElementById('results').style.display = 'none';

    try {
        const response = await fetch('/api/research', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                company_name: companyName,
                depth: depth
            })
        });

        const data = await response.json();

        if (data.success) {
            displayResults(data.results);
        } else {
            alert('Error: ' + data.error);
        }
    } catch (error) {
        alert('Error performing research: ' + error.message);
    } finally {
        document.getElementById('loading').style.display = 'none';
    }
}

async function loadDashboardData() {
    try {
        const response = await fetch('/api/dashboard-data');
        const data = await response.json();

        if (data.success) {
            // Update stats if available
            if (data.stats) {
                updateStats(data.stats);
            }
        }
    } catch (error) {
        console.error('Error loading dashboard data:', error);
    }
}

function displayResults(results) {
    document.getElementById('results').style.display = 'block';

    // Calculate total reviews
    let totalReviews = 0;
    let sentimentCounts = { positive: 0, negative: 0, neutral: 0 };
    const platformData = {};

    for (const [source, data] of Object.entries(results.sources)) {
        totalReviews += data.count;
        platformData[source] = data.count;
    }

    // Update stats
    document.getElementById('total-reviews').textContent = totalReviews;
    document.getElementById('sources-count').textContent = Object.keys(results.sources).length;

    // Display AI analysis if available
    if (results.analysis) {
        displayAnalysis(results.analysis);

        // Update risk level
        const riskLevel = results.analysis.risk_level || 'low';
        const riskElement = document.getElementById('risk-level');
        riskElement.textContent = riskLevel.charAt(0).toUpperCase() + riskLevel.slice(1);
        riskElement.className = 'stat-number badge-' + riskLevel;
    }

    // Create charts
    createSentimentChart(sentimentCounts);
    createPlatformChart(platformData);

    // Display recent reviews
    displayRecentReviews(results.sources);

    // Display generated responses
    if (results.responses) {
        displayGeneratedResponses(results.responses);
    }
}

function displayAnalysis(analysis) {
    // Display key insights
    if (analysis.key_insights) {
        const insightsHtml = analysis.key_insights.map(insight =>
            `<div class="insight-item">${insight}</div>`
        ).join('');
        document.getElementById('ai-insights').innerHTML = insightsHtml;
    }

    // Display critical issues
    if (analysis.critical_issues && analysis.critical_issues.length > 0) {
        const issuesHtml = analysis.critical_issues.map(issue =>
            `<div class="issue-item"><span class="badge badge-high">HIGH</span> ${issue}</div>`
        ).join('');
        document.getElementById('critical-issues').innerHTML = issuesHtml;
    } else {
        document.getElementById('critical-issues').innerHTML = '<p>No critical issues identified.</p>';
    }

    // Display recommendations
    if (analysis.recommendations) {
        const recsHtml = analysis.recommendations.map(rec =>
            `<div class="recommendation-item">${rec}</div>`
        ).join('');
        document.getElementById('recommendations').innerHTML = recsHtml;
    }

    // Update sentiment score
    if (analysis.overall_sentiment) {
        const sentimentMap = {
            'positive': '85%',
            'mixed': '50%',
            'neutral': '50%',
            'negative': '25%'
        };
        document.getElementById('sentiment-score').textContent =
            sentimentMap[analysis.overall_sentiment] || '50%';
    }
}

function displayRecentReviews(sources) {
    let allReviews = [];

    for (const [source, data] of Object.entries(sources)) {
        const reviews = data.data.slice(0, 10); // Top 10 from each source
        reviews.forEach(review => {
            review.platform = source;
            allReviews.push(review);
        });
    }

    // Sort by date if available
    allReviews = allReviews.slice(0, 20); // Show top 20

    const reviewsHtml = allReviews.map(review => {
        const text = review.review || review.text || review.snippet || '';
        const rating = review.rating ? '⭐'.repeat(Math.floor(review.rating)) : '';
        const sentiment = determineSentiment(review.rating);

        return `
            <div class="review-card ${sentiment}">
                <div class="review-header">
                    <span class="review-platform">${review.platform}</span>
                    <span class="review-rating">${rating}</span>
                </div>
                <div class="review-text">${text}</div>
                <div class="review-author">
                    ${review.user || review.author || 'Anonymous'} -
                    ${formatDate(review.date || review.created_at)}
                </div>
            </div>
        `;
    }).join('');

    document.getElementById('recent-reviews').innerHTML = reviewsHtml || '<p>No reviews available.</p>';
}

function displayGeneratedResponses(responses) {
    let responsesHtml = '';

    for (const [source, sourceResponses] of Object.entries(responses)) {
        sourceResponses.slice(0, 5).forEach(resp => {
            responsesHtml += `
                <div class="review-card">
                    <div class="review-header">
                        <span class="review-platform">${source}</span>
                        <span class="badge badge-${resp.sentiment}">${resp.sentiment}</span>
                    </div>
                    <div class="review-text"><strong>Original:</strong> ${resp.original_text}</div>
                    <div class="response-card">
                        <div class="response-label">AI-Generated Response:</div>
                        ${resp.generated_response}
                    </div>
                </div>
            `;
        });
    }

    document.getElementById('generated-responses').innerHTML = responsesHtml || '<p>No responses generated.</p>';
}

function createSentimentChart(sentimentCounts) {
    const ctx = document.getElementById('sentiment-chart').getContext('2d');

    if (sentimentChart) {
        sentimentChart.destroy();
    }

    sentimentChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Positive', 'Negative', 'Neutral'],
            datasets: [{
                data: [
                    sentimentCounts.positive || 30,
                    sentimentCounts.negative || 20,
                    sentimentCounts.neutral || 50
                ],
                backgroundColor: ['#28a745', '#dc3545', '#ffc107']
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'bottom'
                }
            }
        }
    });
}

function createPlatformChart(platformData) {
    const ctx = document.getElementById('platform-chart').getContext('2d');

    if (platformChart) {
        platformChart.destroy();
    }

    platformChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: Object.keys(platformData).map(formatPlatformName),
            datasets: [{
                label: 'Number of Reviews',
                data: Object.values(platformData),
                backgroundColor: '#667eea'
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

function updateStats(stats) {
    if (stats.total_reviews) {
        document.getElementById('total-reviews').textContent = stats.total_reviews;
    }
}

function determineSentiment(rating) {
    if (!rating) return 'neutral';
    if (rating >= 4) return 'positive';
    if (rating <= 2) return 'negative';
    return 'neutral';
}

function formatDate(dateString) {
    if (!dateString) return 'Unknown date';
    try {
        const date = new Date(dateString);
        return date.toLocaleDateString();
    } catch {
        return dateString;
    }
}

function formatPlatformName(platform) {
    return platform.split('_').map(word =>
        word.charAt(0).toUpperCase() + word.slice(1)
    ).join(' ');
}
