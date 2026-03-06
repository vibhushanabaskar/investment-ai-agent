def debate_decision(bull, bear):

    bull_score = bull.get("bull_score", 50)
    bear_score = bear.get("bear_score", 50)

    diff = bull_score - bear_score

    if diff >= 15:
        return "BUY"

    elif diff <= -15:
        return "SELL"

    return "HOLD"