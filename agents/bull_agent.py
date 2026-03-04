from core.llm import call_llm

def bull_case(ticker, indicators, sentiment):

    prompt = f"""
You are bullish.

Stock: {ticker}
Indicators: {indicators}
Sentiment: {sentiment}

Return JSON:
{{
 "bull_score": 0-100,
 "argument": "short reason"
}}
"""

    return call_llm(prompt)