from core.llm import call_llm

def bear_case(ticker, indicators, sentiment):

    prompt = f"""
You are bearish.

Stock: {ticker}
Indicators: {indicators}
Sentiment: {sentiment}

Return JSON:
{{
 "bear_score": 0-100,
 "argument": "short reason"
}}
"""

    return call_llm(prompt)