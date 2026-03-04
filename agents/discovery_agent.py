import yfinance as yf
from agents.technical_agent import get_technical_indicators

# Small stock universe for demo
WATCHLIST = [
    "AAPL","MSFT","TSLA","NVDA","AMD",
    "GOOGL","AMZN","META","NFLX","INTC"
]

def discover_opportunities():

    opportunities = []

    for ticker in WATCHLIST:

        try:
            indicators = get_technical_indicators(ticker)

            score = 0

            if indicators["price"] > indicators["SMA_20"]:
                score += 1

            if indicators["price"] > indicators["SMA_50"]:
                score += 1

            if score >= 2:
                opportunities.append({
                    "ticker": ticker,
                    "score": score,
                    "price": indicators["price"]
                })

        except:
            continue

    return opportunities