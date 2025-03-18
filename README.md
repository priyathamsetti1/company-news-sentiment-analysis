# News Sentiment Analysis and Topic Extraction

## Project Overview
This project is designed to fetch the latest news articles related to a specified company from Google News RSS feeds. It processes the articles to extract key details, perform sentiment analysis, identify important topics, and generate concise summaries. 

### Key Functionalities:
- **News Extraction:** Fetches the top 10 news articles from Google News RSS for a given company.
- **Sentiment Analysis:** Uses VADER Sentiment Analyzer to classify news articles as Positive, Negative, or Neutral.
- **Topic Extraction:** Implements KeyBERT to extract key topics from article summaries.
- **Text Summarization:** Utilizes the BART Transformer model for text summarization.
- **Language Filtering:** Ensures that only English-language articles are processed.

## Dependencies
Before running the project, ensure the following dependencies are installed:

### Required Libraries:
You can install all dependencies using the following command:
```sh
pip install feedparser langdetect vaderSentiment keybert transformers torch requests
```

| Dependency       | Purpose |
|-----------------|-------------------------------------------------|
| `feedparser`    | Fetches and parses RSS feeds for news articles |
| `langdetect`    | Detects the language of the news article summary |
| `vaderSentiment` | Performs sentiment analysis using VADER |
| `keybert`       | Extracts key topics from text using NLP |
| `transformers`  | Provides pre-trained NLP models for summarization |
| `torch`         | Required for running transformer-based models |
| `requests`      | Handles HTTP requests for API integration (if needed) |

## Setup Instructions

### 1. Install Python
Ensure you have **Python 3.8 or later** installed. You can check your Python version by running:
```sh
python --version
```

### 2. Install Dependencies
Run the following command to install all required libraries:
```sh
pip install feedparser langdetect vaderSentiment keybert transformers torch requests
```

### 3. Run the Script
Create a new Python script (e.g., `news_analysis.py`) and copy the following code into it:

```python
import feedparser
from langdetect import detect, LangDetectException
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from keybert import KeyBERT
from transformers import pipeline

# Initialize components
analyzer = SentimentIntensityAnalyzer()
kw_model = KeyBERT()
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def analyze_sentiment(text: str) -> str:
    """Determines the sentiment of a given text using VADER."""
    score = analyzer.polarity_scores(text)
    return "Positive" if score["compound"] >= 0.05 else "Negative" if score["compound"] <= -0.05 else "Neutral"

def extract_topics(text: str) -> list:
    """Extracts key topics from a given text using KeyBERT."""
    return kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 2), stop_words="english", top_n=5)

def summarize_text(text: str) -> str:
    """Summarizes the input text using a pre-trained BART model."""
    if len(text.split()) > 50:
        return summarizer(text, max_length=50, min_length=25, do_sample=False)[0]["summary_text"]
    return text

def fetch_news(company: str):
    """Fetches and processes news articles for a given company."""
    feed = feedparser.parse(f"https://news.google.com/rss/search?q={company}")
    news = []
    
    for entry in feed.entries[:10]:
        try:
            if detect(entry.summary) == "en":
                sentiment = analyze_sentiment(entry.summary)
                topics = [kw[0] for kw in extract_topics(entry.summary)]
                summary = summarize_text(entry.summary)

                news.append({
                    "title": entry.title,
                    "summary": summary,
                    "sentiment": sentiment,
                    "topics": topics,
                    "link": entry.link
                })
        except LangDetectException:
            continue

    return news

# Example Execution
if __name__ == "__main__":
    company_name = "Tesla"
    news_data = fetch_news(company_name)
    for article in news_data:
        print(article)
```

### 4. Running the Script
Save the script and run it using:
```sh
python news_analysis.py
```

## Expected Output
For each news article, the script will return structured JSON data like:
```json
{
  "title": "Tesla’s New Innovation in EVs",
  "summary": "Tesla has unveiled a new battery technology...",
  "sentiment": "Positive",
  "topics": ["Tesla", "battery technology", "EV market"],
  "link": "https://example.com/tesla-news"
}
```

## Deployment Options
This project can be deployed as:
- **Web API using FastAPI**: Create an endpoint that returns processed news data.
- **Streamlit Dashboard**: Display news articles, sentiment, and topics in an interactive UI.
- **Hugging Face Spaces Deployment**: Host the model for easy access.

## Future Enhancements
- Integrate real-time news updates using APIs.
- Improve topic extraction using advanced NLP models.
- Extend support for multilingual news sentiment analysis.

## Contribution
Feel free to contribute by adding new features or optimizing existing ones. Fork the repository and submit pull requests!

## License
This project is open-source and available under the MIT License.

