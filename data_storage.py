import pandas as pd

def save_data(df, file_path):
    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    cleaned_df = pd.read_csv('cleaned_covid_data.csv')
    print(cleaned_df.head())  # Debugging print
    save_data(cleaned_df, 'final_covid_data.csv')
    print("Data saved successfully")
