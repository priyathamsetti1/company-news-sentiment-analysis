# News Summarization and Text-to-Speech Application with stock recommendation system

## Objective
In today's fast-paced digital world, businesses and individuals need to stay
informed about company news which helps to determine future trends in
the stocks of the comapany. However, analyzing multiple news articles
manually is time-consuming. This project automates the process by
summarizing news articles, analyzing their sentiment, and providing text-
to-speech (TTS) conversion in Hindi and also predict the stock prices of the
company based on the overall sentimental summary and provide stock
recommendations.
Overview
This application allows users to input a company name, fetches related news
articles, performs sentiment analysis, and provides a comparative analysis.
Additionally, the summarized content is converted into Hindi speech using
a TTS model and also predict the stock prices and provides stock
recommendations.

## Features

1. **News Extraction**: Extract and display the title, summary, and relevant metadata from at least 10 unique news articles.
2. **Sentiment Analysis**: Analyze article content for sentiment (Positive, Negative, Neutral).
3. **Stock recommendation**:Stock recommendation based on the overall sentiment analysis.
4. **Comparative Analysis**: Compare sentiment across articles for insights on news coverage variations.
5. **Text-to-Speech**: Convert summarized content into Hindi speech using an open-source TTS model.
6. **User Interface**: Streamlit or Gradio-based UI for easy interaction.
7. **API Development**: Frontend and backend communication via APIs.
8. **Deployment**: Hosted on Hugging Face Spaces.
9. **Documentation**: Detailed README explaining implementation, dependencies, and setup.

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
**Code Structure**

**app.py (Frontend & Integration)**
- Handles user input via Streamlit.
- Calls backend APIs for news fetching, summarization, sentiment
    analysis, and TTS.
- Displays results interactively.
  ```
# Set up API base URL (different for local vs production)
if os.environ.get("ENVIRONMENT") == "production":
    API_BASE_URL = os.environ.get("API_URL", "https://your-deployed-api-url")
else:
    API_BASE_URL = "http://127.0.0.1:8000"

# Hero Section with enhanced UI
st.markdown("""
<div class="hero">
    <h1>Company News Sentiment Analysis</h1>
    <p>Get real-time insights into public sentiment about companies with our advanced AI-powered analysis tool.</p>
</div>
""", unsafe_allow_html=True)

# Search Bar with enhanced UI
# Modify your search bar section like this
st.markdown('<div class="search-container">', unsafe_allow_html=True)
col1, col2= st.columns([5, 1])
with col1:
    company_name = st.text_input(
        "", 
        placeholder="Enter company name (e.g., Tesla, Microsoft)", 
        label_visibility="collapsed", 
        key="company_input"
    )

with col2:
    analyze_button = st.button("Analyze")

            
st.markdown('</div>', unsafe_allow_html=True)


# Main Analysis Logic
if analyze_button and company_name:
    with st.spinner("Fetching news and analyzing sentiment..."):
        try:
            # Fetch data from FastAPI backend
            response = requests.get(f"{API_BASE_URL}/news", params={"company": company_name.replace(" ", "")})
            if response.status_code == 200:
                data = response.json()
                
                # Check if articles exist
                if not data.get("Articles"):
                    st.warning(f"No significant news coverage found for {company_name},please try again with another company.")
                else:
                    # Create DataFrame for analysis
                    df = pd.DataFrame(data["Articles"])
                    sentiment_mapping = {"Positive": 1, "Neutral": 0, "Negative": -1}
                    df["sentiment_score"] = df["Sentiment"].map(sentiment_mapping)
                    
                    # Calculate sentiment statistics
                    sentiment_counts = df["Sentiment"].value_counts()
                    total_articles = len(df)
                    positive_percent = round(
                        (sentiment_counts.get("Positive", 0) / total_articles) * 100, 
                        1
                    )
                    negative_percent = round(
                        (sentiment_counts.get("Negative", 0) / total_articles) * 100, 
                        1
                    )
                    neutral_percent = round(
                        (sentiment_counts.get("Neutral", 0) / total_articles) * 100, 
                        1
                    )
                    
                    # Display summary statistics
                    st.markdown('<div class="stats-container">', unsafe_allow_html=True)
                    col1, col2, col3, col4 = st.columns(4)
                    
                    with col1:
                        st.markdown(f"""
                        <div class="stat-card">
                            <div class="value">{total_articles}</div>
                            <div class="label">Total Articles</div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with col2:
                        st.markdown(f"""
                        <div class="stat-card" style="background: linear-gradient(to right, #4caf50, #81c784);">
                            <div class="value" style="color: white;">{positive_percent}%</div>
                            <div class="label" style="color: rgba(255,255,255,0.8);">Positive</div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with col3:
                        st.markdown(f"""
                        <div class="stat-card" style="background: linear-gradient(to right, #9e9e9e, #bdbdbd);">
                            <div class="value" style="color: white;">{neutral_percent}%</div>
                            <div class="label" style="color: rgba(255,255,255,0.8);">Neutral</div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with col4:
                        st.markdown(f"""
                        <div class="stat-card" style="background: linear-gradient(to right, #f44336, #e57373);">
                            <div class="value" style="color: white;">{negative_percent}%</div>
                            <div class="label" style="color: rgba(255,255,255,0.8);">Negative</div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    # Display summaries
                    st.markdown('<div class="summary-container">', unsafe_allow_html=True)
                    st.subheader("📊 Sentiment Analysis Summary:")
                    final_sentiment = data["Final Sentiment Analysis"]
                    st.subheader("🚀 "+final_sentiment)
                    st.subheader("📈 stock recomendation:")
                    final_sentiment = data["Final Sentiment Analysis"]
                    if "positive" in final_sentiment.lower():
                        st.subheader("🟢 BUY RECOMMENDATION: Positive sentiment suggests potential stock growth.")
                    elif "negative" in final_sentiment.lower():
                        st.subheader("🔴 SELL RECOMMENDATION: Negative sentiment indicates potential stock decline.")
                    else:
                        st.subheader("🟡 HOLD RECOMMENDATION: Neutral sentiment suggests maintaining current position.")
                    
                    st.markdown('<div class="audio-container"><h3>🔊 Listen to Summary</h3></div>', unsafe_allow_html=True)
                    audio_base64 = data.get('AudioBase64', '')
                    if audio_base64:
                        # Create a base64 audio HTML element
                        audio_html = f"""
                        <audio controls>
                            <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
                            Your browser does not support the audio element.
                        </audio>
                        """
                        st.markdown(audio_html, unsafe_allow_html=True)
                    else:
                        st.warning("Audio summary not available.")
                    
                    st.write("")
                    
                    # Create visualization tabs with advanced UI
                    tab1, tab2, tab3, tab4 = st.tabs([
                        "📰 News Articles", 
                        "📈 Sentiment Analysis", 
                        "☁️ Word Cloud", 
                        "📊 Coverage Differences"
                    ])
                    
                    with tab1:
                        # Display News Articles with enhanced UI
                        for idx, article in enumerate(data["Articles"]):
                            sentiment_class = article['Sentiment'].lower()
                            sentiment_width = (
                                "100%" 
                                if sentiment_class in ["positive", "negative"] 
                                else "50%"
                            )
                            sentiment_color = {
                                "positive": "#4caf50", 
                                "neutral": "#9e9e9e", 
                                "negative": "#f44336"
                            }.get(sentiment_class, "#9e9e9e")
                            
                            st.markdown(f"""
                            <div class="result-card" style="border-left: 4px solid {sentiment_color};">
                                <h3>{article['Title']}</h3>
                                <p>{article['Summary']}</p>
                                <div class="sentiment-info">
                                    <span class="sentiment-label {sentiment_class}">{article['Sentiment']}</span>
                                    <div class="sentiment-bar"><div class="{sentiment_class}" style="width: {sentiment_width}"></div></div>
                                </div>
                                <p><strong>Topics:</strong> {', '.join(article['Topics'])}</p>
                            </div>
                            """, unsafe_allow_html=True)
                    
                    with tab2:
                        # Enhanced Sentiment Visualization with Plotly
                        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                        
                        # Create two columns for charts
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            # Sentiment Distribution - Pie Chart
                            st.subheader("Sentiment Distribution")
                            fig = px.pie(
                                names=sentiment_counts.index, 
                                values=sentiment_counts.values,
                                color=sentiment_counts.index,
                                color_discrete_map={
                                    "Positive": "#4caf50", 
                                    "Neutral": "#9e9e9e", 
                                    "Negative": "#f44336"
                                },
                                hole=0.4
                            )
                            fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
                            st.plotly_chart(fig, use_container_width=True)
                        
                        with col2:
                            # Sentiment Trend Line Chart
                            st.subheader("Sentiment Trend")
                            fig = px.line(
                                df, x=df.index, y="sentiment_score", 
                                markers=True,
                                color_discrete_sequence=["#2563eb"],
                                labels={
                                    "sentiment_score": "Sentiment (-1 to 1)", 
                                    "index": "Article Index"
                                }
                            )
                            fig.add_hline(y=0, line_dash="dash", line_color="gray")
                            fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
                            st.plotly_chart(fig, use_container_width=True)
                        
                        # Sentiment over time heatmap
                        st.subheader("Sentiment Intensity")
                        df['abs_score'] = df['sentiment_score'].abs()
                        fig = px.bar(
                            df, x=df.index, y='abs_score',
                            color='Sentiment',
                            color_discrete_map={
                                "Positive": "#4caf50", 
                                "Neutral": "#9e9e9e", 
                                "Negative": "#f44336"
                            },
                            labels={
                                "abs_score": "Intensity", 
                                "index": "Article Index"
                            }
                        )
                        fig.update_layout(margin=dict(t=10, b=0, l=0, r=0))
                        st.plotly_chart(fig, use_container_width=True)
                        st.markdown('</div>', unsafe_allow_html=True)
                    
                    with tab3:
                        # Advanced Word Cloud with filters
                        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                        st.subheader("Common Keywords in Articles")
                        
                        text = " ".join(
                            article 
                            for article in df["Summary"].fillna("") 
                            if article
                        )
                        if text.strip():
                            # Generate word cloud with sentiment-based color map
                            wordcloud = WordCloud(
                                width=800, height=400, 
                                background_color="white", 
                                colormap="viridis",
                                max_words=100, 
                                contour_width=1, 
                                contour_color='steelblue'
                            ).generate(text)
                            
                            fig, ax = plt.subplots(figsize=(10, 5))
                            ax.imshow(wordcloud, interpolation="bilinear")
                            ax.axis("off")
                            st.pyplot(fig)
                        else:
                            st.info("No descriptions available to generate a word cloud.")
                        st.markdown('</div>', unsafe_allow_html=True)
                    
                    with tab4:
                        # Display Coverage Differences as Cards
                        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                        st.subheader("📊 Coverage Differences")
                        
                        if "Coverage Differences" in data["Comparative Sentiment Score"]:
                            for diff in data["Comparative Sentiment Score"]["Coverage Differences"]:
                                # Determine sentiment color
                                sentiment_color = (
                                    "#f44336" 
                                    if "uncertainty" in diff["Stock Impact"].lower() 
                                    else "#4caf50"
                                )
                                
                                st.markdown(f"""
                                <div class="result-card" style="border-left: 4px solid {sentiment_color};">
                                    <h3>Comparison: {diff['Comparison']}</h3>
                                    <p><strong>Sentiment Impact:</strong> {diff['Sentiment Impact']}</p>
                                    <p><strong>Stock Impact:</strong> {diff['Stock Impact']}</p>
                                </div>
                                """, unsafe_allow_html=True)
                        else:
                            st.info("No coverage differences found.")
                        st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.warning(f"No significant news coverage found for {company_name},please try again with another company.")
        except Exception as e:
            st.error(f"An error occurred: {e},please try again.")
    
elif analyze_button:
    st.warning("Please enter a company name.")
```
```

**backend.py (Core Processing)**

- Orchestrates API calls to perform various tasks.
- Ensures smooth communication between components.
```
@app.get("/news")
async def get_news(company: str = Query(..., description="Enter company name")):
    """
    Fetch and analyze news for a given company.

    Args:
        company (str): Name of the company to search for.

    Returns:
        dict: Comprehensive news analysis and sentiment report.
    """
    cache_key = company.lower().strip()
    current_time = time.time()

    # Return cached result if available and not expired
    if (cache_key in NEWS_CACHE and
            (current_time - NEWS_CACHE[cache_key]["timestamp"]) < CACHE_EXPIRY):
        return NEWS_CACHE[cache_key]["data"]

    # Fetch fresh data asynchronously
    articles = await asyncio.to_thread(fetch_news, company)

    if not articles:
        result = _create_empty_result(company)
        NEWS_CACHE[cache_key] = {
            "data": result,
            "timestamp": current_time
        }
        return result

    # Sentiment and Topic Analysis
    sentiment_counts, structured_articles, analysis_result = _process_articles(
        articles, company
    )

    # Generate audio as base64 string asynchronously
    audio_base64 = await generate_audio(analysis_result["Final Sentiment Analysis"])

    result = {
        "Company": company,
        "Articles": structured_articles,
        "Comparative Sentiment Score": {
            "Sentiment Distribution": sentiment_counts,
            "Coverage Differences": analysis_result.get("Coverage Differences", []),
            "Topic Overlap": analysis_result.get("Topic Overlap", {})
        },
        "Final Sentiment Analysis": analysis_result["Final Sentiment Analysis"],
        "Audio": "",
        "AudioBase64": audio_base64
    }

    # Cache the result
    NEWS_CACHE[cache_key] = {
        "data": result,
        "timestamp": current_time
    }

    return result


def _create_empty_result(company: str) -> dict:
    """
    Create an empty result when no articles are found.

    Args:
        company (str): Company name.

    Returns:
        dict: Empty result dictionary.
    """
    return {
        "Company": company,
        "Articles": [],
        "Comparative Sentiment Score": {
            "Sentiment Distribution": {"Positive": 0, "Negative": 0, "Neutral": 0},
            "Topic Overlap": {"Common Topics": [], "Unique Topics": {}}
        },
        "Final Sentiment Analysis": f"No significant news coverage found for {company}.",
        "Audio": "",
        "AudioBase64": ""
    }


def _process_articles(articles: list, company: str) -> tuple:
    """
    Process articles for sentiment and topic analysis.

    Args:
        articles (list): List of news articles.
        company (str): Company name.

    Returns:
        tuple: Sentiment counts, structured articles, and analysis results.
    """
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
    structured_articles = []
    all_topics = []
    topic_sets = []
    unique_topics = {}

    for article in articles:
        sentiment = analyze_sentiment(article["summary"])
        article["sentiment"] = sentiment
        sentiment_counts[sentiment] += 1
        all_topics.extend(article["topics"])
        topic_sets.append(set(article["topics"]))

    # Topic frequency and analysis
    topic_freq = Counter(all_topics)
    common_topics = {
        topic for topic, freq in topic_freq.items() if freq > 1
    } or set(topic_freq.keys())

    for i, article in enumerate(articles):
        unique_topics[f"Unique Topics in Article {i+1}"] = list(
            set(article["topics"]) - common_topics
        )

    # Coverage differences
    coverage_differences = _generate_coverage_differences(articles)

    # Structured articles
    for article in articles:
        structured_articles.append({
            "Title": article["title"],
            "Summary": article["summary"],
            "Sentiment": article["sentiment"],
            "Topics": article["topics"],
        })

    # Sentiment and stock prediction
    dominant_sentiment = max(sentiment_counts, key=sentiment_counts.get)
    stock_prediction = _get_stock_prediction(dominant_sentiment)
    sentiment_summary = (
        f"Final Sentiment Analysis: {company}'s latest news coverage is "
        f"mostly {dominant_sentiment}. {stock_prediction}"
    )

    return sentiment_counts, structured_articles, {
        "Final Sentiment Analysis": sentiment_summary,
        "Coverage Differences": coverage_differences,
        "Topic Overlap": {
            "Common Topics": list(common_topics),
            **unique_topics
        }
    }
```

**news_fetcher.py (News Extraction)**
```
- Uses Feedparser and web scraping techniques like BeautifulSoup
    to extract news articles.
- Retrieves metadata such as title, summary, and source.
```
def fetch_news(company: str) -> list:
    """
    Fetch and analyze news articles for a given company.

    Args:
        company (str): The name of the company to fetch news for.

    Returns:
        list: A list of dictionaries containing news article details.
    """
    feed = feedparser.parse(f"https://news.google.com/rss/search?q={company}")
    news = []

    for entry in feed.entries[:10]:
        try:
            if detect(entry.summary) == "en":
                summary = summarize_text(entry.summary)
                topics = extract_topics(summary)
                additional_topics = extract_additional_topics(entry.link)
                sentiment = analyze_sentiment(summary)

                news.append({
                    "title": entry.title,
                    "summary": summary,
                    "sentiment": sentiment,
                    "topics": topics + additional_topics,  # Combine topics
                    "link": entry.link
                })
        except LangDetectException:
            continue  # Skip if language detection fails

    return news


def extract_additional_topics(url: str) -> list:
    """
    Extract additional topics from the news article using Beautiful Soup.

    Args:
        url (str): The URL of the news article.

    Returns:
        list: A list of additional topics extracted from the article.
    """
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Example: Extracting keywords from meta tags
        keywords = soup.find("meta", attrs={"name": "keywords"})
        if keywords:
            return [keyword.strip() for keyword in keywords["content"].split(",")]

        # You can add more extraction logic here as needed
    except Exception as e:
        print(f"Error fetching additional topics: {e}")

    return []
```

**sentiment_analysis.py (Sentiment Computation)**

- Uses NLP models (VADER, DistilBERT) for sentiment classification.
- Outputs sentiment scores and classification (Positive, Negative,
    Neutral).
def analyze_sentiment(text: str) -> str:
    """
    Analyze sentiment of given text.

    Args:
        text (str): Input text to analyze.

    Returns:
        str: Sentiment classification (Positive/Negative/Neutral).
    """
    score = ANALYZER.polarity_scores(text)
    if score["compound"] >= 0.05:
        return "Positive"
    elif score["compound"] <= -0.05:
        return "Negative"
    return "Neutral"


def extract_topics(text: str) -> list:
    """
    Extract top keywords from text.

    Args:
        text (str): Input text to extract keywords from.

    Returns:
        list: Top 5 keywords/keyphrases.
    """
    return [kw[0] for kw in KW_MODEL.extract_keywords(
        text,
        keyphrase_ngram_range=(1, 2),
        stop_words="english",
        top_n=5
    )]


def summarize_text(text: str) -> str:
    """
    Summarize text if longer than 50 words.

    Args:
        text (str): Input text to summarize.

    Returns:
        str: Summarized text or original text if too short.
    """
    if len(text.split()) > 50:
        return SUMMARIZER(
            text,
            max_length=50,
            min_length=25,
            do_sample=False
        )[0]["summary_text"]
    return text
```
**requirements.tx**

- Lists all required dependencies for the project.
- Ensures consistency across installations.
```
fastapi
uvicorn
beautifulsoup4
requests
nltk
transformers
torch
numpy
pandas
scikit-learn
gtts
gradio
streamlit
textblob
deep-translator
feedparser
langdetect
wordcloud
seaborn 
matplotlib 
vaderSentiment
plotly
keybert
langdetect 
torchvision
torchaudio
beautifulsoup4
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
    "Company": "tesla",
    "Articles": [
        {
            "Title": "Tesla owners are trading in their EVs at record levels, Edmunds says - CNBC",
            "Summary": "<a href=\"https://news.google.com/rss/articles/CBMipwFBVV95cUxPVU1YNm10bkFHTDliYUpLd2tqWmdpR0pkX2MzcWJrOUx6akllTVRVYlhYaHljZlV2NHZ5aVprRlhrZkZNVF9YQ2NIX3liRURBUUFSd094N2R1OTBCYlh1aDdqa29EQnNXdDZCNUdfenJsLVc0Uko0SDVhbnJpVGxtY1JpcEVPOE14bVV2NmpLcnVuRG1Zc2J3NTFCMDFzRzJDTjBZZW9CWdIBrAFBVV95cUxPbXBMS3FHaEVNTzVpV1dNdTJOaDZIeUFvM2xUM1B3elhBZUh2elVIUWpnUW5mVXkxNDcyclROV1BleWtVX2FIdXlWMk8tc0drQ1Z6dl9KamxGenlUcjg1X2dTdWl6QXVvWVlDWXdLMXZJWmY2bzVEd1J1WWhnZlBvblRJSl90MFJIcF9hcDhoQW5hdExjb0lkYmtFWkI5eEtNMVhJVXNKb2hibDJq?oc=5\" target=\"_blank\">Tesla owners are trading in their EVs at record levels, Edmunds says</a>&nbsp;&nbsp;<font color=\"#6f6f6f\">CNBC</font>",
            "Sentiment": "Neutral",
            "Topics": [
                "_blank tesla",
                "tesla",
                "trading evs",
                "tesla owners",
                "evs record"
            ]
        },
        {
            "Title": "Tesla Recalls Nearly All Cybertrucks Over Stainless Steel Panels Falling Off - The New York Times",
            "Summary": "<a href=\"https://news.google.com/rss/articles/CBMifEFVX3lxTE43aTloZ2UwSzVQSWdTMTRTSXp6Tko3VlFGVlJUcjlzdDdOMzhMZ0xvS1ppZkItLWxZX3ZxU2U3RUlSSlhVdDRWd1JTZ2RscUVka3JaUFMyWXpJU21GVl92OVpreGs4RHlCdjAzZnZqeUI2V1hzQ25GRVlXM2I?oc=5\" target=\"_blank\">Tesla Recalls Nearly All Cybertrucks Over Stainless Steel Panels Falling Off</a>&nbsp;&nbsp;<font color=\"#6f6f6f\">The New York Times</font>",
            "Sentiment": "Negative",
            "Topics": [
                "tesla recalls",
                "_blank tesla",
                "tesla",
                "cybertrucks stainless",
                "steel panels"
            ]
        },
        {
            "Title": "Tesla Recalls Most Cybertrucks - The Wall Street Journal",
            "Summary": "<a href=\"https://news.google.com/rss/articles/CBMif0FVX3lxTE92a3NRMVg5cGlDMVdNS1h1OFhLdmpYc0g4NWhBYmlqX0NfcWNoY0hySXV0UmJ3Q2xNMllrSkdOSlk0dk9jYWZQNDZrWUZjNDAtUm03TUhvTkhEaFNYMVhCeWZDVVo3dGN1TVRNQ2tEWDFOMV8teUE5ZlZZczFYbkE?oc=5\" target=\"_blank\">Tesla Recalls Most Cybertrucks</a>&nbsp;&nbsp;<font color=\"#6f6f6f\">The Wall Street Journal</font>",
            "Sentiment": "Neutral",
            "Topics": [
                "_blank tesla",
                "tesla",
                "tesla recalls",
                "recalls cybertrucks",
                "cybertrucks"
            ]
        },
        {
            "Title": "In latest blow to Tesla, regulators recall nearly all Cybertrucks - The Associated Press",
            "Summary": "<a href=\"https://news.google.com/rss/articles/CBMioAFBVV95cUxNWVlJUGRoV0hpRHhsV0liSXpjZlM5UHU0TnluclM1eTVTeDVsRUwyTjhMT3ZScGtrNl9BX1hQcE0zRWhWSW5pcXg5aF9uSF9yaVh2TVJMdjNjWEktenBCc09JRVpXWnRTVmVwRW9HaFdiUVYzQjl3ZnM4N3dSS190WG8wZjlGeWdQMmVzcVdaQWlhc2RoNTMwcnBOWjRKZ29E?oc=5\" target=\"_blank\">In latest blow to Tesla, regulators recall nearly all Cybertrucks</a>&nbsp;&nbsp;<font color=\"#6f6f6f\">The Associated Press</font>",
            "Sentiment": "Neutral",
            "Topics": [
                "tesla regulators",
                "tesla",
                "regulators recall",
                "cybertrucks",
                "nearly cybertrucks"
            ]
        },
        {
            "Title": "Tesla faces a ‘brand crisis tornado.’ The one guy who can fix it is MIA - CNN",
            "Summary": "<a href=\"https://news.google.com/rss/articles/CBMiiAFBVV95cUxPZXhtVEIyNWJ4RzlQMDJNYVJsRVJNOG9Xek95MENndk1TZExpdjhxMXBfcjlwMWd0X2NqSDVQSVA4M1EzTW5QLUNUSlZ2OWpkVF8wR05RYjA1X0MxdmhqeFRwTTZJdENxVFFnU2lhR2ZidllieG4wajdteE1ZYWtsV3pjVVZhcGdY0gF_QVVfeXFMUEZWS1QzZTBweVk3YU5UclRKYldCU2twcWJBVU9UNnpaSkx5UXNEazlSVlpUUWJFVHFtRFp3ZWxSWTQ3eW9xeUFNRnJzQUxFTWVJZXBGek1ZVC1BbHZjeVVKSG5BNGJuMFIzN0FMNDl2TmI2QTRtUVN1eE55Z0dKYw?oc=5\" target=\"_blank\">Tesla faces a ‘brand crisis tornado.’ The one guy who can fix it is MIA</a>&nbsp;&nbsp;<font color=\"#6f6f6f\">CNN</font>",
            "Sentiment": "Negative",
            "Topics": [
                "_blank tesla",
                "tesla faces",
                "tesla",
                "href",
                "crisis tornado"
            ]
        },
        {
            "Title": "US attorney general to bring charges for Tesla damage, citing ‘domestic terrorism’ - The Guardian US",
            "Summary": "<ol><li><a href=\"https://news.google.com/rss/articles/CBMiiAFBVV95cUxON2k5bUJaSGJNRjBFcURIWndSQkN4a2dnR0Fna1hid05waEwzOF9FaFlMSTBUQXotQk5aanpSeUFMQnFXU3FSSVBxMU5YWnZOMUlFeHEyd2FqLUNKakVMc0dFdEtyVllqbjFHUkxKTjN3NmVxTnRSNE0xakZBeHBFMG13dTF1MlBM?oc=5\" target=\"_blank\">US attorney general to bring charges for Tesla damage, citing ‘domestic terrorism’</a>&nbsp;&nbsp;<font color=\"#6f6f6f\">The Guardian US</font></li><li><a href=\"https://news.google.com/rss/articles/CBMingFBVV95cUxNRWtsajg1czZPUmhkVjJmNWxlSTQ1OXpYcmxhRGRvdGRHWFhVTGJsQWE3d3NfTi1UbC10SUxRZlRobDN1em1uR3FmcWl3dVY3bElOaWk0SDFJMy1Zd1hwVno3OVA2NlQ3T0FOWXhRMmhEU1lUQi0xd05hRktHZG53ZDJQa1FWbTRrVmlUeGt2cTgxb29EQXNJVFdGR3NOZw?oc=5\" target=\"_blank\">3 people face federal charges for Tesla attacks. Are such acts domestic terrorism?</a>&nbsp;&nbsp;<font color=\"#6f6f6f\">NPR</font></li><li><a href=\"https://news.google.com/rss/articles/CBMiugFBVV95cUxPd2w2OXUxemxKTjNpTkxCV003MFlzOW5HLVBnNGw3b0pNTzJuT01QNVprWnI1Slg2Z0VWNDlfTDRSemN0dXFFZ1BMWEFjQ3hZcUJOMjhodmYzZjlYVjRwMGg5RnFjdWFBVGNESmVrMkROM2V0SnZDelN5Yms5c1RYcE5TdlUzTEpEVHhINk4wWlJ1TXlidHUybkM5UFUyWkNINzdMaVkzV2ZnZm1RZWZPcHFtdXRHY3o1TGfSAb8BQVVfeXFMTlNZMDRzUDl2UVFxT2Ffb09RQmtuYU1GQkxpVzR4OWw4M3hfLTVZeTBRMHhGc29nNXpZdzh5NzNFTWItZEVSME9TVFozaFEyN0R1YjJNVlk1Z0t5VHBqSVcwdkRyeUpqOTJXRGdOSEtIUnAtbTZNV0NuQ2pnUTRTdzE5VHBwZTA5MTlZdXB1U1dvcHQwWDJGTWdLMDRNeDVpaExPMXpFWGxwNFppckgwSmRJYkRkc0JRRjZ4VlZfRFk?oc=5\" target=\"_blank\">Dems who have spoken passionately against domestic terrorism go silent as Tesla torchers are charged</a>&nbsp;&nbsp;<font color=\"#6f6f6f\">Fox News</font></li></ol>",
            "Sentiment": "Negative",
            "Topics": [
                "tesla attacks",
                "domestic terrorism",
                "attacks acts",
                "charges tesla",
                "tesla damage"
            ]
        },
        {
            "Title": "Lutnick urges Fox News viewers to buy Tesla stock, raising ethics questions - The Washington Post",
            "Summary": "<ol><li><a href=\"https://news.google.com/rss/articles/CBMiwgFBVV95cUxNcGU1RkRnVE1FXzFiMXo3REJKQUE5anZmNFJ4SHVpU2RfRFZGemZGVjdLUWdpd0xZWnFvYVltZmFaZ0lqTEM5TjVwMHV1TFRROXFiR191SmNCelptNEF2enZWRGJtMDE2X3Bwdkp6d1pHc1JJTXJiR2JJR1VYUVpOUFFZaU4xc2Yza2RFTUF6YjVJajVnQ0JBbk1EaVpSS05RSzBqclZIa3AydHd0TUVqYmZCeFhnZWlHTEN4dk5tMXVqQQ?oc=5\" target=\"_blank\">Lutnick urges Fox News viewers to buy Tesla stock, raising ethics questions</a>&nbsp;&nbsp;<font color=\"#6f6f6f\">The Washington Post</font></li><li><a href=\"https://news.google.com/rss/articles/CBMie0FVX3lxTFBtZTlnVS1heVJCVTZSLUJqS0pJa0lobm9PZWZ2SkR3ZlN1LWV3bEtuV2szRG1ZcFpyWkMtTEdBY0ZGcWNSNVZ4eGI4VGpvV2dkZXIwaHc4cjllWWI1VnM2MkZNSG5KLU8xWFh1aHRLa1JDdXgtaTdnemJtVQ?oc=5\" target=\"_blank\">Lutnick’s Pitch to Buy Tesla Stock Is Unprecedented and Alarming, Historians Say</a>&nbsp;&nbsp;<font color=\"#6f6f6f\">Barron's</font></li><li><a href=\"https://news.google.com/rss/articles/CBMiuAFBVV95cUxOcGcwQzlEOExuRGJBWUhkVzdhSnIyYVlwNEJwOFBTVllpbl9lNDg1RHEtU0xSSmhFYVJaZGlfTTlPTVFCZzhiZHhzTUJ2ek9MZ1NNMURnYTdKU3YxaDJDMHo2TkNKRUZkQzBRWVRJOFN2bVdDWWg4TTd6ek8wNGYwYTE2WmRqWlBkUW1WYmprNFRTd3R2WUNOTFdTYXpZTEJ0S1haUzJGV18wY2NNSE1pNGFQMHcxU2FK?oc=5\" target=\"_blank\">Musk Tells Tesla Employees Hang On to Stock After 50% Plunge</a>&nbsp;&nbsp;<font color=\"#6f6f6f\">Bloomberg</font></li></ol>",
            "Sentiment": "Negative",
            "Topics": [
                "tesla stock",
                "tells tesla",
                "tesla employees",
                "buy tesla",
                "stock unprecedented"
            ]
        },
        {
            "Title": "80 Teslas damaged at Hamilton dealership, largest car vandalism reported in Canada against the U.S. company - CBC.ca",
            "Summary": "<a href=\"https://news.google.com/rss/articles/CBMiiwFBVV95cUxQS3hVbnFLN2ltXzV5Ui1Jc0s5Y0EwSjZEeV8yQlAyTHJSYm8ta1hBcTFfVnpyX2lCX1JYZkJiZlA3STVUU0Nfb2Z1Z2ZKMU5xeTdLeEJHUlFuRFA0RnBMbEZDX1VXZXhxV2tid3FYYmo2X25uaWI0MFBOT1dsejdTVFhfWnBCbE1RUzJJ0gFHQVVfeXFMTVMyRWotRHFmdEtSWTNnNUdVZ241QTlWbWdOeTctWGJ0Ry1vcTY1cWt1REVIdjJUZ2lMczBVWnQ3cTJWVWtYLVU?oc=5\" target=\"_blank\">80 Teslas damaged at Hamilton dealership, largest car vandalism reported in Canada against the U.S. company</a>&nbsp;&nbsp;<font color=\"#6f6f6f\">CBC.ca</font>",
            "Sentiment": "Negative",
            "Topics": [
                "teslas damaged",
                "car vandalism",
                "damaged hamilton",
                "teslas",
                "vandalism reported"
            ]
        },
        {
            "Title": "Tesla Vandalism Surges in Canada as Trump and Musk Face Backlash - The New York Times",
            "Summary": "<a href=\"https://news.google.com/rss/articles/CBMijAFBVV95cUxQLTNHZU5GZXl5YVluUmpzdkxvR3oxY2FxZWxhVjl2UTJWTXpWY0FoX1VKMTRsTV9fbFMwMHFDMmVnbVVIU1lLdnZNTHA3WHhVNDVpQ2dCNUlMTkJzOVNKSFhtRGNZNGs1OHdXOW00TThxREZfaWxnQTQtX3BsUWJ1ems2TU1ucmZabUlvZg?oc=5\" target=\"_blank\">Tesla Vandalism Surges in Canada as Trump and Musk Face Backlash</a>&nbsp;&nbsp;<font color=\"#6f6f6f\">The New York Times</font>",
            "Sentiment": "Neutral",
            "Topics": [
                "tesla vandalism",
                "_blank tesla",
                "trump musk",
                "musk face",
                "href"
            ]
        },
        {
            "Title": "Tesla owners alarmed by Dogequest website listing personal information - NBC News",
            "Summary": "<a href=\"https://news.google.com/rss/articles/CBMingFBVV95cUxQa3NBMkxkS3pYQzBVVlVqWWVTYmlGem51cFJJVGJnMjg0WFhPMlByTUh0WXh0c3dHRDVFNVNtQjlpdkFYTGNmeXdjenNzVzJTV0xzXzVEbG9uSTM4ekdvSF96LUxxalE2S2dOR0dCTTRpd3dXU1VjdTRCVmkxS0xUdkJFNlNqRVFxcXNvaFR6NXRhdW9YU2QySk9wYnlUUdIBVkFVX3lxTE1FcEJlaVFKLS1vcnZxZFdQM05OSklPa0R4QlpNNVg1bHVEV3lJTDZmWW5BNW13QWtsMS02R1lYdFNSSUdtOVJ1MU9GTFN4aXpFdU5MRmZB?oc=5\" target=\"_blank\">Tesla owners alarmed by Dogequest website listing personal information</a>&nbsp;&nbsp;<font color=\"#6f6f6f\">NBC News</font>",
            "Sentiment": "Negative",
            "Topics": [
                "_blank tesla",
                "tesla owners",
                "tesla",
                "dogequest website",
                "alarmed dogequest"
            ]
        }
    ],
    "Comparative Sentiment Score": {
        "Sentiment Distribution": {
            "Positive": 0,
            "Negative": 6,
            "Neutral": 4
        },
        "Coverage Differences": [
            {
                "Comparison": "Article 1 covers ['_blank tesla', 'tesla', 'trading evs', 'tesla owners', 'evs record'], while Article 2 focuses on ['tesla recalls', '_blank tesla', 'tesla', 'cybertrucks stainless', 'steel panels'].",
                "Sentiment Impact": "Article 1 has a Neutral sentiment, while Article 2 has a Negative sentiment.",
                "Stock Impact": "This may create uncertainty in stock trends."
            },
            {
                "Comparison": "Article 2 covers ['tesla recalls', '_blank tesla', 'tesla', 'cybertrucks stainless', 'steel panels'], while Article 3 focuses on ['_blank tesla', 'tesla', 'tesla recalls', 'recalls cybertrucks', 'cybertrucks'].",
                "Sentiment Impact": "Article 2 has a Negative sentiment, while Article 3 has a Neutral sentiment.",
                "Stock Impact": "This may create uncertainty in stock trends."
            },
            {
                "Comparison": "Article 3 covers ['_blank tesla', 'tesla', 'tesla recalls', 'recalls cybertrucks', 'cybertrucks'], while Article 4 focuses on ['tesla regulators', 'tesla', 'regulators recall', 'cybertrucks', 'nearly cybertrucks'].",
                "Sentiment Impact": "Article 3 has a Neutral sentiment, while Article 4 has a Neutral sentiment.",
                "Stock Impact": "The sentiment consistency may stabilize stock movements."
            },
            {
                "Comparison": "Article 4 covers ['tesla regulators', 'tesla', 'regulators recall', 'cybertrucks', 'nearly cybertrucks'], while Article 5 focuses on ['_blank tesla', 'tesla faces', 'tesla', 'href', 'crisis tornado'].",
                "Sentiment Impact": "Article 4 has a Neutral sentiment, while Article 5 has a Negative sentiment.",
                "Stock Impact": "This may create uncertainty in stock trends."
            },
            {
                "Comparison": "Article 5 covers ['_blank tesla', 'tesla faces', 'tesla', 'href', 'crisis tornado'], while Article 6 focuses on ['tesla attacks', 'domestic terrorism', 'attacks acts', 'charges tesla', 'tesla damage'].",
                "Sentiment Impact": "Article 5 has a Negative sentiment, while Article 6 has a Negative sentiment.",
                "Stock Impact": "The sentiment consistency may stabilize stock movements."
            },
            {
                "Comparison": "Article 6 covers ['tesla attacks', 'domestic terrorism', 'attacks acts', 'charges tesla', 'tesla damage'], while Article 7 focuses on ['tesla stock', 'tells tesla', 'tesla employees', 'buy tesla', 'stock unprecedented'].",
                "Sentiment Impact": "Article 6 has a Negative sentiment, while Article 7 has a Negative sentiment.",
                "Stock Impact": "The sentiment consistency may stabilize stock movements."
            },
            {
                "Comparison": "Article 7 covers ['tesla stock', 'tells tesla', 'tesla employees', 'buy tesla', 'stock unprecedented'], while Article 8 focuses on ['teslas damaged', 'car vandalism', 'damaged hamilton', 'teslas', 'vandalism reported'].",
                "Sentiment Impact": "Article 7 has a Negative sentiment, while Article 8 has a Negative sentiment.",
                "Stock Impact": "The sentiment consistency may stabilize stock movements."
            },
            {
                "Comparison": "Article 8 covers ['teslas damaged', 'car vandalism', 'damaged hamilton', 'teslas', 'vandalism reported'], while Article 9 focuses on ['tesla vandalism', '_blank tesla', 'trump musk', 'musk face', 'href'].",
                "Sentiment Impact": "Article 8 has a Negative sentiment, while Article 9 has a Neutral sentiment.",
                "Stock Impact": "This may create uncertainty in stock trends."
            },
            {
                "Comparison": "Article 9 covers ['tesla vandalism', '_blank tesla', 'trump musk', 'musk face', 'href'], while Article 10 focuses on ['_blank tesla', 'tesla owners', 'tesla', 'dogequest website', 'alarmed dogequest'].",
                "Sentiment Impact": "Article 9 has a Neutral sentiment, while Article 10 has a Negative sentiment.",
                "Stock Impact": "This may create uncertainty in stock trends."
            }
        ],
        "Topic Overlap": {
            "Common Topics": [
                "_blank tesla",
                "href",
                "cybertrucks",
                "tesla owners",
                "tesla",
                "tesla recalls"
            ],
            "Unique Topics in Article 1": [
                "trading evs",
                "evs record"
            ],
            "Unique Topics in Article 2": [
                "cybertrucks stainless",
                "steel panels"
            ],
            "Unique Topics in Article 3": [
                "recalls cybertrucks"
            ],
            "Unique Topics in Article 4": [
                "nearly cybertrucks",
                "tesla regulators",
                "regulators recall"
            ],
            "Unique Topics in Article 5": [
                "crisis tornado",
                "tesla faces"
            ],
            "Unique Topics in Article 6": [
                "attacks acts",
                "tesla damage",
                "tesla attacks",
                "domestic terrorism",
                "charges tesla"
            ],
            "Unique Topics in Article 7": [
                "tells tesla",
                "stock unprecedented",
                "tesla stock",
                "buy tesla",
                "tesla employees"
            ],
            "Unique Topics in Article 8": [
                "teslas",
                "car vandalism",
                "teslas damaged",
                "vandalism reported",
                "damaged hamilton"
            ],
            "Unique Topics in Article 9": [
                "musk face",
                "tesla vandalism",
                "trump musk"
            ],
            "Unique Topics in Article 10": [
                "dogequest website",
                "alarmed dogequest"
            ]
        }
    },
    "Final Sentiment Analysis": "Final Sentiment Analysis: tesla's latest news coverage is mostly Negative. Stock prices may decrease.",
    "Audio": "",
    "AudioBase64": "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RFs66LSgVubkOAF8tb02u/2dv38rcT/D//OExOsxm/JwAOYW3P3/4//ga/7hjfXcDUVcC/nzBTxqJ1+1izO3rKui5wJoba54tlWU3mFE1ike/pu9qtiHAUNcaioglhe8wqlTzR5zy5hpxNnX/0////+/VpiMil0Qgx99/tsj5/uzOcaPHmONz6nG6tms/q51jDzDDmYueeYWJv2PLor90AoAHTB5EltIf8xg6NbcEf5p3GW95hSRb95tbju/bZt7vC+8Y3e1N0pSeW98MNewHWiYMI60skVO//OExNcnI/qEAOPO3K9wUScUDCYYtzk8c8Rn7+Ozt8ejBP8sZv/OX6ZisatflmikgrLxoKw/YXEgQIIrihguQWMMQdTi5iJLIQOdEl7qbR76LP0qEqX0TqW5cYKJ769JMChNDx7wO//m93RKe9PabeayjIiKhOUi70RLl59EiVhmKgbN+QlKlLts7KkA15QSJSZtkOxig6vHOrQ93vd7+tlLL5c7z849fXWNf19cTaiML/bXHRqGIpIMTeo4a0n3//OExO0s4+qIANvQ3DJcfhujXEHYGEA4D0P8t06GQKwlOqGlTl6aE0a50AO53CygjQjofBeyG7PUnASAlD5FnPF2hkZLK46iWD4V51ptToxWajdYVch7qZNEsV0SMZ7elUwhKQXarhq6r9eViGK1iY9t7E9gLEed4yOnNeePYbBjN0RFzqHCvLLbNFRDdq6Pp5deiqxrjvuxu4Fa13bU99YYJNW3iaDiVWQoma7lg/cJ5Bzt62RfeZ+34v48sZt3//OExOw91CKIANPe3Zfv4E+aZpB3HIKwKkc8CHZQTTP3rfz9d5/73zn97z+63//nruGrM/QVs62V+hu5YcztyGmsPDTPqqrafqhg+U43qfdmA6sorRZ5IcdqBFhIeXm5bQiIj1DyNYjFttwfA0Fh8eDuICpDHiA7H86D50/Cg1XCTAUh3DguFR5OlckdiyA9MPhJMziMzhi9E+R00UaUvA0KA7oy2hNpCWS0mk8QzvFPxJ1UWUO/WUW7JX9fi+kH//OExKc07AKgABYY3WMW2121zE0gyqOrFYypFjLdntfipLufW94LsVjjl1H7lvbrd+3T2QTngQ2fVb//////+3UiCraoRURFMInGAMALB4ODhELUe6sYUaOVsK4WHSYXGYhDwBsalY/l58dV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"
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
