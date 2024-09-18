# Redbus Data Scraping and Analysis

## Project Overview

This project automates the extraction, cleaning, and analysis of bus travel data from Redbus. It combines web scraping with Selenium, data processing with pandas, database management with MySQL, and visualization through Streamlit to provide a comprehensive tool for analyzing bus travel information.

## Project Structure

The repository includes the following files:

- **`bus_routes.ipynb`**: Jupyter Notebook for scraping initial bus route data.
- **`busdetails.ipynb`**: Jupyter Notebook for extracting detailed bus information.
- **`data_cleaning.ipynb`**: Jupyter Notebook for cleaning and preprocessing the scraped data.
- **`store_data_to_sql.py`**: Python script for storing the cleaned data in a MySQL database.
- **`streamlit.py`**: Python script for creating an interactive dashboard with Streamlit.

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- MySQL server
- Necessary Python libraries: `selenium`, `pandas`, `mysql-connector-python`, `sqlalchemy`, `streamlit`, `Pillow`

Install the required Python libraries using pip:
    ```pip install selenium pandas mysql-connector-python sqlalchemy streamlit pillow```


## Setup and Installation

### 1. Data Scraping

- **Run `bus_routes.ipynb`**:
  - This notebook scrapes basic bus route data, including state names, routes, and links to detailed bus information.
  
- **Run `busdetails.ipynb`**:
  - This notebook scrapes detailed information about each bus from the links obtained in the previous step.

### 2. Data Cleaning

- **Run `data_cleaning.ipynb`**:
  - This notebook processes the raw data to handle missing values, remove duplicates, and ensure data consistency.

### 3. Store Data

- **Configure MySQL Database**:
  - Ensure MySQL server is running and accessible. Adjust database credentials in `store_data_to_sql.py` as needed.

- **Run `store_data_to_sql.py`**:
  - This script creates the database and table, and inserts the cleaned data into the MySQL database. It also optimizes performance by temporarily disabling indexes.

### 4. Data Visualization

- **Run `streamlit.py`**:
  - Launch an interactive dashboard to explore and filter bus data. Start the Streamlit app using the following command:
  
  ```bash
  streamlit run streamlit.py

## Detailed Explanation

### Data Scraping

- **`bus_routes.ipynb`**: 
  - Gathers initial bus route data from Redbus, focusing on route and link information.
  
- **`busdetails.ipynb`**: 
  - Extracts comprehensive details about each bus, including names, types, timings, and prices.

### Data Cleaning

- **`data_cleaning.ipynb`**: 
  - Cleans the dataset by addressing missing values, removing duplicates, and formatting columns for consistency.

### Database Storage

- **`store_data_to_sql.py`**: 
  - Connects to a MySQL database, creates the necessary database and table, and inserts the cleaned data into the table. This script also optimizes performance by temporarily disabling indexes.

### Interactive Dashboard

- **`streamlit.py`**: 
  - Provides an interactive web interface for data exploration. Users can filter data based on various criteria such as state, bus name, price range, and star rating.

## Contribution

Contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request.

## Contact

For further questions or feedback, please contact [Yogesh R] at [yogeshprabu11@gmail.com].
