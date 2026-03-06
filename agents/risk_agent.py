def assess_risk(indicators):

    price = indicators["price"]
    sma20 = indicators["SMA_20"]
    sma50 = indicators["SMA_50"]

    if price < sma50:
        return "HIGH"

    if price < sma20:
        return "MEDIUM"

    return "LOW"