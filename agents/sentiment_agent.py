import requests
from core.config import NEWS_API_KEY
from core.llm import call_llm

def analyze_sentiment(ticker):

    url = f"https://newsapi.org/v2/everything?q={ticker}&language=en&apiKey={NEWS_API_KEY}"
    res = requests.get(url).json()

    headlines = "\n".join([a["title"] for a in res.get("articles", [])[:5]])

    prompt = f"""
Return JSON:
{{
 "sentiment_score": -1 to 1,
 "summary": "short summary"
}}

News:
{headlines}
"""

    return call_llm(prompt)