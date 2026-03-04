import yfinance as yf
import pandas as pd

def get_technical_indicators(ticker):

    df = yf.download(ticker, period="3mo", auto_adjust=True, progress=False)

    if df.empty:
        raise ValueError(f"No data returned for {ticker}")

    # Flatten columns if multi-index
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df["SMA_20"] = df["Close"].rolling(20).mean()
    df["SMA_50"] = df["Close"].rolling(50).mean()

    latest = df.iloc[-1]

    return {
        "price": float(latest["Close"]),
        "SMA_20": float(latest["SMA_20"]) if not pd.isna(latest["SMA_20"]) else 0,
        "SMA_50": float(latest["SMA_50"]) if not pd.isna(latest["SMA_50"]) else 0
    }