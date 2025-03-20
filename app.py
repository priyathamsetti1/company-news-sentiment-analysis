"""
Streamlit Application for Company News Sentiment Analysis.

This module sets up the backend server and configures the Streamlit page.
"""
import os
import threading

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import requests
import streamlit as st
import uvicorn
from backend import app
from wordcloud import WordCloud


def run_fastapi() -> None:
    """
    Run FastAPI server in a separate thread.

    Starts the backend server on localhost at port 8000.
    """
    uvicorn.run(app, host="127.0.0.1", port=8000)


# Start FastAPI server in a background thread
BACKEND_THREAD = threading.Thread(target=run_fastapi, daemon=True)
BACKEND_THREAD.start()

# Configure page settings
st.set_page_config(
    page_title="Company News Sentiment Analysis", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# Enhanced CSS with modern design elements
st.markdown("""
    <style>
    *, *::before, *::after { 
        box-sizing: border-box; 
        margin: 0; 
        padding: 0; 
    }
    
    body { 
        font-family: 'Inter', system-ui, sans-serif; 
        color: #D0ECE7; 
        width: 100%; 
    }
    
    .stApp { 
        background: #D0ECE7; 
    }
    
    .hero h1 { 
        font-size: 3rem; 
        background: linear-gradient(to right, #2563eb, #4f46e5); 
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent; 
        font-weight: 800; 
        margin-bottom: 1rem; 
    }
    
    .hero p { 
        font-size: 1.25rem; 
        color: #6b7280; 
        margin-bottom: 1.5rem; 
    }
    
    .feature-card, .result-card, .chart-container { 
        background: rgba(255, 255, 255, 0.9); 
        padding: 1.5rem; 
        border-radius: 0.75rem; 
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); 
        margin-bottom: 1.5rem; 
        border: 1px solid #e5e7eb; 
        transition: transform 0.3s; 
    }
    
    .feature-card:hover, .result-card:hover { 
        transform: translateY(-5px); 
        box-shadow: 0 8px 12px -1px rgba(0, 0, 0, 0.15); 
    }
    
    .feature-card h3, .result-card h3 { 
        font-size: 1.5rem; 
        color: #1f2937; 
        margin-bottom: 1rem; 
    }
    
    .feature-card p, .result-card p { 
        color: #6b7280; 
        line-height: 1.5; 
        margin-bottom: 0.5rem; 
    }
    
    .sentiment-label { 
        display: inline-block; 
        padding: 0.25rem 0.75rem; 
        border-radius: 1rem; 
        font-weight: 500; 
        margin-bottom: 0.5rem; 
    }
    
    .sentiment-label.positive { 
        background-color: rgba(76, 175, 80, 0.1); 
        color: #4caf50; 
    }
    
    .sentiment-label.negative { 
        background-color: rgba(244, 67, 54, 0.1); 
        color: #f44336; 
    }
    
    .sentiment-label.neutral { 
        background-color: rgba(158, 158, 158, 0.1); 
        color: #9e9e9e; 
    }
    
    .sentiment-bar { 
        height: 6px; 
        background: rgba(0, 0, 0, 0.1); 
        border-radius: 3px; 
        overflow: hidden; 
        margin-bottom: 1rem; 
    }
    
    .sentiment-bar .positive { 
        background-color: #4caf50; 
        height: 100%; 
        width: 100%; 
    }
    
    .sentiment-bar .negative { 
        background-color: #f44336; 
        height: 100%; 
        width: 100%; 
    }
    
    .sentiment-bar .neutral { 
        background-color: #9e9e9e; 
        height: 100%; 
        width: 50%; 
    }
    
    .section-title { 
        text-align: center; 
        font-size: 2rem; 
        margin-bottom: 1.5rem; 
        color: #1f2937; 
    }
    
    .search-container { 
        max-width: 700px; 
        margin: 0 auto 1.5rem; 
        display: flex; 
        flex-direction: row; 
        align-items: center;
        background: white !important;
        padding: 0.5rem;
        border-radius: 0.5rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    .stButton>button { 
        background: linear-gradient(to right, #2563eb, #4f46e5);
        color: white; 
        border-radius: 0.5rem; 
        font-weight: 600; 
        border: none; 
        height: 38px; 
        margin-top: 0; 
        padding: 0 1.5rem; 
    }
    
    .audio-container { 
        margin: 1.5rem 0; 
        text-align: center; 
        background: white;
        padding: 1rem;
        border-radius: 0.75rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    audio { 
        width: 100%; 
        max-width: 500px; 
        margin: 0 auto; 
    }
    
    .stTabs [data-baseweb="tab-list"] { 
        gap: 1rem; 
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: white;
        border-radius: 4px 4px 0px 0px;
        gap: 1rem;
        padding: 10px 16px;
        font-weight: 500;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #4f46e5 !important;
        color: white !important;
    }
    
    .summary-container {
        background: white;
        padding: 1.5rem;
        border-radius: 0.75rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-bottom: 1.5rem;
    }
    
    .stats-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin-bottom: 1.5rem;
    }
    
    .stat-card {
        background: white;
        padding: 1rem;
        border-radius: 0.5rem;
        text-align: center;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    .stat-card .value {
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .stat-card .label {
        color: #6b7280;
        font-size: 0.9rem;
    }
    
    .loader {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 200px;
    }
    </style>
    """, unsafe_allow_html=True)


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
                    st.warning(f"No significant news coverage found for {company_name}.")
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
                    st.subheader("📊 Sentiment Analysis Summary")
                    final_sentiment = data["Final Sentiment Analysis"]
                    st.write(final_sentiment)
                    st.subheader("📈 stock recomendation")
                    final_sentiment = data["Final Sentiment Analysis"]
                    if "positive" in final_sentiment.lower():
                        st.write("🟢 BUY RECOMMENDATION: Positive sentiment suggests potential stock growth.")
                    elif "negative" in final_sentiment.lower():
                        st.write("🔴 SELL RECOMMENDATION: Negative sentiment indicates potential stock decline.")
                    else:
                        st.write("🟡 HOLD RECOMMENDATION: Neutral sentiment suggests maintaining current position.")
                    
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
                st.error(f"Failed to fetch data: {response.status_code}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    
elif analyze_button:
    st.warning("Please enter a company name.")







# Features Section with interactive elements
st.markdown(
    '<h2 class="section-title" id="features">Key Features</h2>', 
    unsafe_allow_html=True
)
feature_cols = st.columns(3)

features = [
    {
        "title": "Real-Time Analysis",
        "description": "Get instant sentiment analysis of recent news articles for any company. Stay on top of market sentiment."
    },
    {
        "title": "Advanced Visualization",
        "description": "Interactive charts and graphs help you understand sentiment trends and patterns at a glance."
    },
    {
        "title": "Multi-language Support",
        "description": "View insights in multiple languages with automatic translation and audio summary capabilities."
    }
]

for i, feature in enumerate(features):
    with feature_cols[i]:
        st.markdown(f"""
        <div class="feature-card">
            <h3>{feature["title"]}</h3>
            <p>{feature["description"]}</p>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 2rem; padding: 1rem; color: #6b7280; font-size: 1.8rem;">
    © 2025 Company News Sentiment Analysis | @priyatham_setti
</div>
""", unsafe_allow_html=True)

# Main entry point
if __name__ == "__main__":
    pass