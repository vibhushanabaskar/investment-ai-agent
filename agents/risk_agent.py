def assess_risk(indicators):

    if indicators["price"] < indicators["SMA_50"]:
        return "HIGH"
    if indicators["price"] < indicators["SMA_20"]:
        return "MEDIUM"
    return "LOW"