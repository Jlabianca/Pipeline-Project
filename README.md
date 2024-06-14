# Overview
This project aims to build a data pipeline that extracts, processes and visualizes COVID-19 data from Johns Hopkins University using Python and Tableau. 
The data pipeline is automated to ensure that the latest data is always available for analysis and visualization.

## Project Structure
The project is organized into several scripts, each responsible for a specific part of the data pipeline:

data_extraction.py: Extracts raw COVID-19 data from Johns Hopkins University.
data_cleaning.py: Cleans and transforms the extracted data.
data_storage.py: Stores the cleaned data for analysis and visualization.
automation.py: Automates the data pipeline to run at regular intervals.

## Data Source
The data used in this project is sourced from the [Johns Hopkins University COVID-19 dataset](https://github.com/CSSEGISandData/COVID-19), which provides daily updates on COVID-19 cases worldwide. 
The dataset includes detailed information on confirmed cases, deaths, and recoveries across different regions and countries.

## Break down of the files
 ``` bash
  public_data_pipeline/
  │
  ├── data_extraction.py
  ├── data_cleaning.py
  ├── data_storage.py
  ├── automation.py
  ├── raw_covid_data.csv
  ├── cleaned_covid_data.csv
  └── final_covid_data.csv
 ```
