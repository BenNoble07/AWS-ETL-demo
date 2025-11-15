import pandas as pd

# Load sample CSV
df = pd.read_csv('../data/netflix_sample.csv')

# Simple transformation: rename columns
df = df[['show_id', 'type', 'title', 'release_year', 'rating']]

# Save transformed CSV
df.to_csv('../data/netflix_sample_transformed.csv'', index=False)

print("ETL done!")
