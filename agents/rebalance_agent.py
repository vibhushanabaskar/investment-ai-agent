def rebalance_advice(portfolio_results):

    advice = []

    for stock in portfolio_results:

        if stock["signal"] == "BUY":
            advice.append(f"Consider increasing exposure to {stock['ticker']}")

        elif stock["signal"] == "SELL":
            advice.append(f"Consider reducing exposure to {stock['ticker']}")

    if not advice:
        advice.append("Portfolio allocation looks balanced today.")

    return advice