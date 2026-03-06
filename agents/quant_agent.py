def compute_quant_score(indicators, sentiment, risk):

    price = indicators["price"]
    sma20 = indicators["SMA_20"]
    sma50 = indicators["SMA_50"]

    sentiment_score = sentiment.get("sentiment_score", 0)

    score = 50  # neutral baseline


    # ---------- Momentum ----------
    if price > sma20:
        score += 10
    else:
        score -= 10

    if price > sma50:
        score += 10
    else:
        score -= 10


    # ---------- Trend Strength ----------
    trend_strength = (price - sma50) / sma50

    if trend_strength > 0.05:
        score += 10
    elif trend_strength > 0.02:
        score += 5
    elif trend_strength < -0.05:
        score -= 10
    elif trend_strength < -0.02:
        score -= 5


    # ---------- Sentiment ----------
    if sentiment_score > 0.4:
        score += 10
    elif sentiment_score > 0.1:
        score += 5
    elif sentiment_score < -0.4:
        score -= 10
    elif sentiment_score < -0.1:
        score -= 5


    # ---------- Risk Penalty ----------
    if risk == "HIGH":
        score -= 10
    elif risk == "MEDIUM":
        score -= 5


    # clamp to valid range
    score = max(0, min(100, score))

    return round(score, 2)