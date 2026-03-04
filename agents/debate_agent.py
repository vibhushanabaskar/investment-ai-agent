def debate_decision(bull, bear):

    bull_score = bull.get("bull_score", 50)
    bear_score = bear.get("bear_score", 50)

    if bull_score > bear_score + 10:
        return "BUY"
    elif bear_score > bull_score + 10:
        return "SELL"
    return "HOLD"