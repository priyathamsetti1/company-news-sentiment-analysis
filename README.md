# Company News Sentiment Analysis and Summarization with Stock Recommendation System

## Introduction

### Problem Statement
In today's fast-paced digital world, businesses and individuals need to stay informed about company news to determine future stock trends. However, manually analyzing multiple news articles is time-consuming. This project automates the process by summarizing news articles, analyzing their sentiment, and providing text-to-speech (TTS) conversion in Hindi. Additionally, it predicts stock prices based on the overall sentiment and provides stock recommendations.

### Overview
This application allows users to input a company name, fetches related news articles, performs sentiment analysis, and provides a comparative analysis. The summarized content is converted into Hindi speech using a TTS model. The system also predicts stock prices and provides stock recommendations.

## Features

- **Automated News Fetching**: Extracts news articles related to a given company.
- **Summarization**: Uses NLP models to summarize articles.
- **Sentiment Analysis**: Determines whether the news is positive, negative, or neutral.
- **Comparative Sentiment Analysis**: Provides an overview of sentiment trends.
- **Text-to-Speech (TTS)**: Converts summarized content into Hindi speech.
- **User-Friendly Interface**: Built using Streamlit.
- **API-Driven Architecture**: Enables seamless integration with other applications.
- **Deployment**: Hosted on Hugging Face Spaces for accessibility.

## Project Setup

### Prerequisites
- Python 3.8+
- pip package manager
- Internet connection for API and model usage

### Installation Steps

1. **Clone the Repository:**  
   ```bash
   git clone https://github.com/priyathamsetti1/company-news-sentiment-analysis
   cd company-news-sentiment-analysis
   ```

2. **Install Dependencies:**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**  
   ```bash
   streamlit run app.py
   ```

## Code Structure

### `app.py` (Frontend & Integration)
- Handles user input via Streamlit.
- Calls backend APIs for news fetching, summarization, sentiment analysis, and TTS.
- Displays results interactively.

### `backend.py` (Core Processing)
- Orchestrates API calls to perform various tasks.
- Ensures smooth communication between components.

### `news_fetcher.py` (News Extraction)
- Uses Feedparser and web scraping techniques like BeautifulSoup4 to extract news articles.
- Retrieves metadata such as title, summary, and source.

### `sentiment_analysis.py` (Sentiment Computation)
- Uses NLP models (VADER, DistilBERT) for sentiment classification.
- Outputs sentiment scores and classification (Positive, Negative, Neutral).

### `requirements.txt`
- Lists all required dependencies for the project.
- Ensures consistency across installations.

## API Development

The application follows a RESTful API design, enabling modularity and external integrations.

### API Endpoints

| Method | Endpoint             | Functionality |
|--------|----------------------|--------------|
| GET    | `/fetch_news`        | Fetches news articles |
| POST   | `/analyse_sentiment` | Performs sentiment analysis |
| POST   | `/compare_sentiment` | Conducts sentiment comparison |
| POST   | `/generate_tts`      | Converts text to Hindi Speech |

### Accessing APIs

APIs can be tested using Postman or cURL.

Example request:
```bash
curl -X GET "https://priyatahm-news-api.hf.space/news?company=companyname" -H "Content-Type: application/json"
```

## Assumptions & Limitations

- News articles are fetched only from publicly accessible sources.
- Sentiment analysis may not be 100% accurate due to language variations.
- TTS conversion is limited to Hindi only.
- Web scraping might be restricted due to site policies.
- Stock predictions are not 100% accurate.

## Conclusion

This project streamlines the process of gathering and analyzing company-related news, assisting in stock estimation. It integrates NLP, sentiment analysis, and TTS capabilities into a user-friendly application. Future improvements can include multilingual TTS, advanced sentiment models, and expanded news sources.

## Deployment Link
- **Sentiment Analysis API Access Deployment Link:** [https://priyatahm-sentiment-news-analysis.hf.space]

## License
- **MIT License**

## GitHub Repository
- **[GitHub Repo](https://github.com/priyathamsetti1/company-news-sentiment-analysis)**

## Contributors
- **Priyatham Setti**
