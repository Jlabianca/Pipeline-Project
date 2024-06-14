import schedule
import time
from data_extraction import extract_data
from data_cleaning import clean_data
from data_storage import save_data

def job():
    data_df = extract_data()
    cleaned_df = clean_data(data_df)
    save_data(cleaned_df, 'final_covid_data.csv')

schedule.every().day.at("10:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
