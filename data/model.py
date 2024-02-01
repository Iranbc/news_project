# Load csv into df

import pandas as pd

news_df = pd.read_csv("raw/news_dataset.csv")

print(f"shape: {news_df.shape}")

print(f"columns: {news_df.columns}")
