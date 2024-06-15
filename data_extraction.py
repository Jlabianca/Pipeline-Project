import requests
import pandas as pd

def extract_data():
    url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
    
    # Use requests to download the CSV file content
    response = requests.get(url)
    response.raise_for_status()  # Ensure we notice bad responses
    
    # Save the content to a local file
    with open('raw_covid_data.csv', 'wb') as file:
        file.write(response.content)
    
    # Read the CSV file into a DataFrame
    df = pd.read_csv('raw_covid_data.csv')
    return df

if __name__ == "__main__":
    data_df = extract_data()
    data_df.to_csv('raw_covid_data.csv', index=False)
    print(data_df.head())
