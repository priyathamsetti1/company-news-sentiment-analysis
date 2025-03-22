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
### **Expected Output**
```{
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
    "Audio": "summary.mp3"
    
}
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
