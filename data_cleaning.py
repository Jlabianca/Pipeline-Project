import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path)
    # Drop rows with missing values
    df.dropna(inplace=True)
    # Filter for specific years or countries if needed
    df = df[df['date'].astype(int) >= 2000]  # Example filter
    return df

cleaned_df = clean_data('raw_data.csv')
cleaned_df.to_csv('cleaned_data.csv', index=False)
print(cleaned_df.head())
