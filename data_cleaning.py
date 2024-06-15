import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path)
    print(df.columns)  # Print the column names to debug

    # Assuming we want to keep 'country.value', 'date', and 'value' columns
    df = df[['country.value', 'date', 'value']]
    
    # Rename columns to be more intuitive
    df.rename(columns={
        'country.value': 'Country',
        'date': 'Date',
        'value': 'Confirmed'
    }, inplace=True)

    # Convert the 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Drop rows with missing 'Confirmed' values
    df.dropna(subset=['Confirmed'], inplace=True)

    return df

if __name__ == "__main__":
    cleaned_df = clean_data('raw_data.csv')
    if not cleaned_df.empty:
        cleaned_df.to_csv('cleaned_data.csv', index=False)
        print(cleaned_df.head())
    else:
        print("Data cleaning failed due to column name mismatch.")
