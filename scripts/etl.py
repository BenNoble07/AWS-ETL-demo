import pandas as pd

# Load sample CSV
df = pd.read_csv('../data/sample.csv')

# Simple transformation: rename columns
df.rename(columns={'old_col':'new_col'}, inplace=True)

# Save transformed CSV
df.to_csv('../data/sample_transformed.csv', index=False)

print("ETL done!")
