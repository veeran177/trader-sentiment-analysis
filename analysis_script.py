import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Loading Datasets 
sentiment_df = pd.read_csv("fear_greed_index.csv", parse_dates=["date"])
trader_df = pd.read_csv("historical_data.csv")

# Converting Timestamp to Date 
trader_df["date"] = pd.to_datetime(trader_df["Timestamp"], unit="ms").dt.date
sentiment_df["date"] = sentiment_df["date"].dt.date

# Merging Sentiment into Trader Data 
merged_df = pd.merge(trader_df, sentiment_df[["date", "classification"]], on="date", how="left")

# Feature Engineering 
merged_df["is_greed"] = merged_df["classification"].isin(["Greed", "Extreme Greed"]).astype(int)
merged_df["is_fear"] = merged_df["classification"].isin(["Fear", "Extreme Fear"]).astype(int)

# Cleaning numeric columns
merged_df["Closed PnL"] = pd.to_numeric(merged_df["Closed PnL"], errors="coerce")
merged_df["Fee"] = pd.to_numeric(merged_df["Fee"], errors="coerce")

# Aggregation 
daily_stats = (
    merged_df.groupby(["date", "classification"])
    .agg(
        total_trades=("Account", "count"),
        avg_fee=("Fee", "mean"),
        net_pnl=("Closed PnL", "sum"),
        win_rate=("Closed PnL", lambda x: np.mean(x > 0)),
    )
    .reset_index()
)

# Saving Summary 
daily_stats.to_csv("sentiment_trader_summary.csv", index=False)

# Creating Visualizations 
os.makedirs("visualizations", exist_ok=True)

def plot_metric(metric, ylabel, filename):
    plt.figure(figsize=(8, 5))
    sns.barplot(data=daily_stats, x="classification", y=metric, estimator=np.mean, ci=None)
    plt.title(f"Average {ylabel} by Market Sentiment")
    plt.ylabel(ylabel)
    plt.xlabel("Sentiment")
    plt.tight_layout()
    plt.savefig(f"visualizations/{filename}")
    plt.close()

plot_metric("net_pnl", "Net PnL", "pnl_by_sentiment.png")
plot_metric("win_rate", "Win Rate", "winrate_by_sentiment.png")
plot_metric("total_trades", "Trade Count", "trades_by_sentiment.png")

