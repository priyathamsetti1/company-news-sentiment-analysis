# News Summarization and Text-to-Speech Application

## Objective
Develop a web-based application that extracts key details from multiple news articles related to a given company, performs sentiment analysis, conducts a comparative analysis, and generates a text-to-speech (TTS) output in Hindi. The tool allows users to input a company name and receive a structured sentiment report along with an audio output.

## Features

1. **News Extraction**: Extract and display the title, summary, and relevant metadata from at least 10 unique news articles.
2. **Sentiment Analysis**: Analyze article content for sentiment (Positive, Negative, Neutral).
3. **Comparative Analysis**: Compare sentiment across articles for insights on news coverage variations.
4. **Text-to-Speech**: Convert summarized content into Hindi speech using an open-source TTS model.
5. **User Interface**: Streamlit or Gradio-based UI for easy interaction.
6. **API Development**: Frontend and backend communication via APIs.
7. **Deployment**: Hosted on Hugging Face Spaces.
8. **Documentation**: Detailed README explaining implementation, dependencies, and setup.

## Tech Stack

### **Backend Framework**
- FastAPI
- Uvicorn (ASGI server)

### **Programming Language**
- Python

### **Machine Learning & NLP Libraries**
- Transformers (Hugging Face)
- VaderSentiment
- KeyBERT
- LangDetect
- Summarization Pipeline (Facebook BART)

### **Web Scraping & News Fetching**
- Feedparser

### **Frontend Framework**
- Streamlit

### **Data Visualization**
- Plotly Express
- Matplotlib
- Pandas

### **Audio Generation**
- gTTS (Google Text-to-Speech)
- Google Translator

### **Additional Libraries**
- Requests (HTTP requests)
- Base64 (encoding/decoding)
- Threading
- Re (Regular Expressions)

### **Deployment & Hosting**
- Local development with threading
- Hosted on Hugging Face Spaces: [Click Here](https://priyatahm-sentiment-news-analysis.hf.space)

### **Caching**
- In-memory dictionary-based caching

### **Middleware**
- CORS middleware (FastAPI)

## Installation & Setup

### Prerequisites
- Python 3.8+
- Required libraries (installed via `requirements.txt`)

### Steps to Run Locally

1. **Clone the Repository**
   ```bash
   git clone <GitHub-repo-link>
   cd News-Summarization-TTS
   ```
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Application**
   ```bash
   streamlit run app.py
   ```

## API Development
- **API Endpoints**
  - `/fetch_news`: Fetches and extracts news articles.
  - `/analyze_sentiment`: Performs sentiment analysis.
  - `/compare_sentiment`: Conducts comparative analysis.
  - `/generate_tts`: Converts summarized text to Hindi speech.

- **Usage**
  - APIs can be accessed via Postman or any REST client.
  - Example:
    ```bash
    curl -X GET "https://priyatahm-news-api.hf.space/news?company=comapnyname" -d '{"companyname": "Tesla"}' -H "Content-Type: application/json"
    ```

## Model Details
- **Summarization**: Hugging Face Transformers (BART/T5)
- **Sentiment Analysis**: Pretrained NLP model (e.g., VADER, DistilBERT)
- **TTS**: Open-source Hindi TTS model (e.g., Coqui-TTS)

## Expected Output
```
{
  "Company": "Tesla",
  "Articles": [
    {
      "Title": "Tesla's New Model Breaks Sales Records",
      "Summary": "Tesla's latest EV sees record sales in Q3...",
      "Sentiment": "Positive",
      "Topics": ["Electric Vehicles", "Stock Market", "Innovation"]
    },
    {
      "Title": "Regulatory Scrutiny on Tesla's Self-Driving Tech",
      "Summary": "Regulators have raised concerns over Tesla’s self-driving software...",
      "Sentiment": "Negative",
      "Topics": ["Regulations", "Autonomous Vehicles"]
    }
  ],
  "Comparative Sentiment Score": { ... },
  "Final Sentiment Analysis": "Tesla’s latest news coverage is mostly positive. Potential stock growth expected.",
  "Audio": "[Play Hindi Speech]"
}
```

## Assumptions & Limitations
- Only non-JS news websites are scraped (BeautifulSoup used).
- TTS output is limited to Hindi language.
- Sentiment analysis accuracy depends on the dataset used.

## Contribution Guidelines
- Fork the repository and create a feature branch.
- Follow PEP8 guidelines.
- Ensure proper documentation and comments in code.
- Submit a pull request with a detailed explanation.

## License
This project is licensed under the MIT License.

## Acknowledgements
- Hugging Face for NLP models.
- Streamlit/Gradio for UI framework.
- Open-source TTS models for Hindi speech synthesis.
