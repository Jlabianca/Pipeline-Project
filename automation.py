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
        # Step 1: Extract data
        data_df = extract_data()
        logging.info("Data extraction completed")
        logging.info(f"Extracted data: {data_df.head()}")
        
        # Step 2: Clean data
        cleaned_df = clean_data(data_df)
        if cleaned_df.empty:
            logging.warning("Cleaned data is empty")
            return
        logging.info("Data cleaning completed")
        logging.info(f"Cleaned data: {cleaned_df.head()}")
        
        # Step 3: Save data
        save_data(cleaned_df, 'final_covid_data.csv')
        logging.info("Data storage completed")
    except Exception as e:
        logging.error(f"Error occurred: {e}")

# Schedule the job for every minute for testing purposes
schedule.every().day.at("10:00").do(job)

logging.info("Scheduler started")
while True:
    schedule.run_pending()
    time.sleep(1)
