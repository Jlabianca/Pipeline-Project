import pandas as pd

def clean_data(df):
    print(df.columns)  # Print the column names to debug

    # Adjust these columns based on the actual data
    required_columns = {'Province/State', 'Country/Region', 'Lat', 'Long'}
    
    # Print actual column names
    actual_columns = set(df.columns)
    print(f"Actual columns: {actual_columns}")

    if not required_columns.issubset(actual_columns):
        print("Warning: Column names do not match expected names.")
        return pd.DataFrame()  # Return an empty DataFrame or handle accordingly

    df = df.melt(id_vars=list(required_columns), 
                 var_name="Date", 
                 value_name="Confirmed")
    df['Date'] = pd.to_datetime(df['Date'])
    df.dropna(subset=['Confirmed'], inplace=True)
    return df

if __name__ == "__main__":
    raw_df = pd.read_csv('raw_covid_data.csv')
    cleaned_df = clean_data(raw_df)
    if not cleaned_df.empty:
        cleaned_df.to_csv('cleaned_covid_data.csv', index=False)
        print(cleaned_df.head())
    else:
        print("Data cleaning failed due to column name mismatch.")
