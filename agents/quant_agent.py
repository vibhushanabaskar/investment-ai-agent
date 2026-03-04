def compute_quant_score(indicators, sentiment, risk):

    score = 0

    # Momentum factor
    if indicators["price"] > indicators["SMA_20"]:
        score += 30

    if indicators["price"] > indicators["SMA_50"]:
        score += 30

    # Sentiment factor
    sentiment_score = sentiment.get("sentiment_score", 0)

    if sentiment_score > 0.3:
        score += 25
    elif sentiment_score > 0:
        score += 15

    # Risk factor
    if risk == "LOW":
        score += 15
    elif risk == "MEDIUM":
        score += 8

    return min(score, 100)