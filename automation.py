import schedule
import time
import logging
from data_extraction import extract_data
from data_cleaning import clean_data
from data_storage import save_data

# Configure logging
logging.basicConfig(filename='pipeline.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def job():
    logging.info("Job started")
    try:
        data_df = extract_data()
        logging.info("Data extraction completed")
        
        cleaned_df = clean_data(data_df)
        logging.info("Data cleaning completed")
        
        save_data(cleaned_df, 'final_covid_data.csv')
        logging.info("Data storage completed")
    except Exception as e:
        logging.error(f"Error occurred: {e}")

schedule.every(1).minutes.do(job)

logging.info("Scheduler started")
while True:
    schedule.run_pending()
    time.sleep(1)
