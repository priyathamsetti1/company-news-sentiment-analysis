"""Utility Functions for News Sentiment Analysis Project."""

import base64
import asyncio
from io import BytesIO
from typing import Dict, Any, List

from deep_translator import GoogleTranslator
from gtts import gTTS
from langdetect import detect, LangDetectException
from transformers import pipeline
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from keybert import KeyBERT


class SentimentAnalyzer:
    """
    Comprehensive utility class for text analysis and processing.
    """
    def __init__(self):
        """
        Initialize sentiment analysis and text processing tools.
        """
        self.sentiment_analyzer = SentimentIntensityAnalyzer()
        self.keyword_extractor = KeyBERT()
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    def analyze_sentiment(self, text: str) -> str:
        """
        Analyze sentiment of given text.

        Args:
            text (str): Input text to analyze.

        Returns:
            str: Sentiment classification (Positive/Negative/Neutral).
        """
        try:
            score = self.sentiment_analyzer.polarity_scores(text)
            if score["compound"] >= 0.05:
                return "Positive"
            elif score["compound"] <= -0.05:
                return "Negative"
            return "Neutral"
        except Exception as e:
            print(f"Sentiment Analysis Error: {e}")
            return "Neutral"

    def extract_keywords(self, text: str, top_n: int = 5) -> List[str]:
        """
        Extract top keywords from text.

        Args:
            text (str): Input text to extract keywords from.
            top_n (int): Number of keywords to extract.

        Returns:
            list: Top keywords/keyphrases.
        """
        try:
            return [kw[0] for kw in self.keyword_extractor.extract_keywords(
                text,
                keyphrase_ngram_range=(1, 2),
                stop_words="english",
                top_n=top_n
            )]
        except Exception as e:
            print(f"Keyword Extraction Error: {e}")
            return []

    def summarize_text(self, text: str, max_length: int = 50) -> str:
        """
        Summarize text if longer than specified word count.

        Args:
            text (str): Input text to summarize.
            max_length (int): Maximum summary length.

        Returns:
            str: Summarized text or original text.
        """
        try:
            if len(text.split()) > max_length:
                summary = self.summarizer(
                    text,
                    max_length=max_length,
                    min_length=25,
                    do_sample=False
                )[0]["summary_text"]
                return summary
            return text
        except Exception as e:
            print(f"Text Summarization Error: {e}")
            return text

    async def generate_multilingual_audio(
        self, 
        text: str, 
        source_lang: str = "en", 
        target_lang: str = "hi"
    ) -> Dict[str, str]:
        """
        Generate multilingual audio with translation.

        Args:
            text (str): Text to convert to audio.
            source_lang (str): Source language code.
            target_lang (str): Target language code.

        Returns:
            dict: Audio details with base64 encoding.
        """
        try:
            # Translate text
            translated_text = await self._translate_text(text, source_lang, target_lang)

            # Generate audio
            audio_base64 = await self._text_to_speech(
                translated_text, 
                language=target_lang if translated_text != text else source_lang
            )

            return {
                "original_text": text,
                "translated_text": translated_text,
                "audio_base64": audio_base64,
                "source_language": source_lang,
                "target_language": target_lang
            }
        except Exception as e:
            print(f"Multilingual Audio Generation Error: {e}")
            return {}

    async def _translate_text(
        self, 
        text: str, 
        source_lang: str = "en", 
        target_lang: str = "hi"
    ) -> str:
        """
        Translate text between languages.

        Args:
            text (str): Text to translate.
            source_lang (str): Source language code.
            target_lang (str): Target language code.

        Returns:
            str: Translated text.
        """
        try:
            return await asyncio.to_thread(
                GoogleTranslator(source=source_lang, target=target_lang).translate,
                text
            )
        except Exception:
            return text

    async def _text_to_speech(
        self, 
        text: str, 
        language: str = "hi"
    ) -> str:
        """
        Convert text to speech and return base64 encoded audio.

        Args:
            text (str): Text to convert.
            language (str): Language code for TTS.

        Returns:
            str: Base64 encoded audio.
        """
        try:
            mp3_fp = BytesIO()
            tts = await asyncio.to_thread(
                gTTS, 
                text=text, 
                lang=language
            )
            await asyncio.to_thread(tts.write_to_fp, mp3_fp)
            mp3_fp.seek(0)

            audio_bytes = await asyncio.to_thread(mp3_fp.read)
            return base64.b64encode(audio_bytes).decode('utf-8')
        except Exception as e:
            print(f"Text to Speech Error: {e}")
            return ""

# Instantiate utility classes
sentiment_utils = SentimentAnalyzer()
