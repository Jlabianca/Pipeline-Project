import requests
import pandas as pd

def extract_data():
    url = 'http://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?format=json&per_page=1000'
    response = requests.get(url)
    data = response.json()
    
    # Extract relevant data
    df = pd.json_normalize(data[1])
    return df

data_df = extract_data()
data_df.to_csv('raw_data.csv', index=False)
print(data_df.head())
