"""API Module for News Sentiment Analysis Project."""

from typing import List, Dict, Any
from fastapi import APIRouter, Query, HTTPException
from fastapi.responses import JSONResponse

from utils import sentiment_utils
from news_extractor import fetch_news

class NewsAnalysisAPI:
    """
    API Router for News Sentiment Analysis endpoints.
    """
    def __init__(self):
        """
        Initialize API router and cache mechanisms.
        """
        self.router = APIRouter()
        self.news_cache = {}
        self.setup_routes()

    def setup_routes(self):
        """
        Define API routes and their corresponding handlers.
        """
        @self.router.get("/news", response_model=Dict[str, Any])
        async def get_company_news(
            company: str = Query(..., description="Company name for news analysis")
        ):
            """
            Fetch and analyze news for a given company.

            Args:
                company (str): Name of the company.

            Returns:
                dict: Comprehensive news analysis report.
            """
            try:
                # Normalize company name
                company = company.strip().lower()

                # Check cache first
                if company in self.news_cache:
                    return self.news_cache[company]

                # Fetch news
                articles = await fetch_news(company)

                if not articles:
                    return self._create_empty_result(company)

                # Analyze articles
                analysis_result = self._analyze_articles(articles, company)

                # Cache result
                self.news_cache[company] = analysis_result
                return analysis_result

            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        @self.router.get("/audio", response_model=Dict[str, str])
        async def generate_audio(
            text: str = Query(..., description="Text to convert to audio"),
            source_lang: str = Query("en", description="Source language"),
            target_lang: str = Query("hi", description="Target language")
        ):
            """
            Generate multilingual audio for given text.

            Args:
                text (str): Text to convert.
                source_lang (str): Source language code.
                target_lang (str): Target language code.

            Returns:
                dict: Audio generation details.
            """
            try:
                audio_result = await sentiment_utils.generate_multilingual_audio(
                    text, source_lang, target_lang
                )
                return audio_result
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

    def _analyze_articles(self, articles: List[Dict], company: str) -> Dict[str, Any]:
        """
        Comprehensive analysis of news articles.

        Args:
            articles (list): List of news articles.
            company (str): Company name.

        Returns:
            dict: Detailed analysis report.
        """
        analyzed_articles = []
        sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}

        for article in articles:
            # Sentiment and topic analysis
            sentiment = sentiment_utils.analyze_sentiment(article['summary'])
            topics = sentiment_utils.extract_keywords(article['summary'])

            analyzed_article = {
                "title": article['title'],
                "summary": article['summary'],
                "sentiment": sentiment,
                "topics": topics
            }

            analyzed_articles.append(analyzed_article)
            sentiment_counts[sentiment] += 1

        # Generate final sentiment summary
        dominant_sentiment = max(sentiment_counts, key=sentiment_counts.get)
        sentiment_summary = self._generate_sentiment_summary(
            company, dominant_sentiment, sentiment_counts
        )

        return {
            "company": company,
            "articles": analyzed_articles,
            "sentiment_distribution": sentiment_counts,
            "sentiment_summary": sentiment_summary
        }

    def _create_empty_result(self, company: str) -> Dict[str, Any]:
        """
        Create a default result when no news is found.

        Args:
            company (str): Company name.

        Returns:
            dict: Empty analysis result.
        """
        return {
            "company": company,
            "articles": [],
            "sentiment_distribution": {
                "Positive": 0, "Negative": 0, "Neutral": 0
            },
            "sentiment_summary": f"No news found for {company}"
        }

    def _generate_sentiment_summary(
        self, 
        company: str, 
        dominant_sentiment: str, 
        sentiment_counts: Dict[str, int]
    ) -> str:
        """
        Generate a narrative sentiment summary.

        Args:
            company (str): Company name.
            dominant_sentiment (str): Most prevalent sentiment.
            sentiment_counts (dict): Sentiment distribution.

        Returns:
            str: Narrative sentiment summary.
        """
        total_articles = sum(sentiment_counts.values())
        summary_template = (
            f"{company}'s recent news coverage is predominantly {dominant_sentiment}. "
            f"Sentiment Breakdown: "
            f"Positive: {sentiment_counts['Positive']/total_articles*100:.1f}%, "
            f"Neutral: {sentiment_counts['Neutral']/total_articles*100:.1f}%, "
            f"Negative: {sentiment_counts['Negative']/total_articles*100:.1f}%"
        )
        return summary_template

# Create API router instance
news_analysis_api = NewsAnalysisAPI()
router = news_analysis_api.router
