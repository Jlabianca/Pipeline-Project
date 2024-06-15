import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path)
    print(df.columns)  # Print the column names to debug

    # Check for required columns
    required_columns = {'Province/State', 'Country/Region', 'Lat', 'Long'}
    if not required_columns.issubset(df.columns):
        print("Warning: Column names do not match expected names.")
        return pd.DataFrame()  # Return an empty DataFrame or handle accordingly

    df = df.melt(id_vars=["Province/State", "Country/Region", "Lat", "Long"], 
                 var_name="Date", 
                 value_name="Confirmed")
    df['Date'] = pd.to_datetime(df['Date'])
    df.dropna(subset=['Confirmed'], inplace=True)
    return df

if __name__ == "__main__":
    raw_df = pd.read_csv('raw_covid_data.csv')
    cleaned_df = clean_data('raw_covid_data.csv')
    if not cleaned_df.empty:
        cleaned_df.to_csv('cleaned_covid_data.csv', index=False)
        print(cleaned_df.head())
    else:
        print("Data cleaning failed due to column name mismatch.")
