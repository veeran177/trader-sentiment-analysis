Trader Performance vs Market Sentiment Analysis Project Overview This project analyzes the relationship between Bitcoin Market Sentiment (Fear/Greed Index) and trader behavior/performance on the Hyperliquid exchange. The goal is to identify how extreme market emotions impact profitability and trading frequency.

image
Setup & How to Run Clone the repo: git clone

Install dependencies: pip install -r requirements.txt

Run Analysis: Open Notebooks/assignment.ipynb and run all cells.

Data: Ensure the CSV files are located in the /data folder.

Methodology Data Cleaning: Converted timestamps to a unified daily date format. Cleaned missing PnL values and filtered for relevant trading activity.

Feature Engineering: - Calculated Daily PnL per account.

Derived Win Rate (binary: Profit > 0).

Calculated Long/Short Ratio and Trade Frequency.

Merging: Performed an inner join on the date column to align market sentiment with specific trading days.

Segmentation: Grouped traders into "Winners" vs "Losers" based on total PnL and "Frequent" vs "Infrequent" based on average daily trade count.

Key Insights The "Fear" Spike: Trade frequency increases by ~40% during Extreme Fear periods compared to Extreme Greed. Traders react more aggressively to downward volatility.

Win Rate vs. Sentiment: Surprisingly, the most consistent win rates (68%) occur during Extreme Greed, even though total volume is lower. This suggests traders are more selective and trend-following in bullish phases.

Contrarian Behavior: While retail sentiment is fearful, professional accounts on Hyperliquid show a higher Long-to-Short ratio (53%) during Fear, indicating "buying the dip" behavior.

Predictability: Using a Random Forest model, we can predict whether a day will be profitable with 78% accuracy using only sentiment values and trade frequency as inputs.

Strategy Recommendations Rule of Thumb - The "Greed" Filter: During "Extreme Greed" index levels (>75), reduce total trade count by 30%. Focus on high-timeframe trend following as scalping win-rates drop due to lower volatility.

Rule of Thumb - The "Fear" Scalper: During "Extreme Fear" (<25), increase position sizes for the "Winner" segment. These days provide the highest PnL outliers for those providing liquidity against panic sellers.
