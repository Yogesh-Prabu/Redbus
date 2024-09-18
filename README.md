# Redbus Data Scraping and Analysis

This project involves scraping bus travel data from Redbus, cleaning the data, storing it in a SQL database, and visualizing it through an interactive Streamlit dashboard. The objective is to provide a comprehensive tool for analyzing and filtering bus travel information.

## Project Structure

- `bus_routes.ipynb`: Jupyter notebook for scraping bus route data.
- `busdetails.ipynb`: Jupyter notebook for scraping detailed bus information.
- `data_cleaning.ipynb`: Jupyter notebook for cleaning and preprocessing the scraped data.
- `store_data_to_sql.py`: Python script for storing cleaned data into a MySQL database.
- `streamlit.py`: Streamlit application for visualizing and interacting with the data.

## Installation

### Prerequisites

1. **Python 3.x**: Ensure you have Python installed on your machine.
2. **MySQL Server**: Make sure MySQL Server is installed and running.
3. **Required Python Libraries**: Install the required libraries using `pip`.

   ```bash
   pip install pandas selenium mysql-connector-python sqlalchemy streamlit pillow

4. ChromeDriver: Download and install ChromeDriver compatible with your Chrome version.


## Setting Up

### Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>

Prepare the Database
Ensure MySQL Server is running.
Update store_data_to_sql.py with your database credentials.
Create the database by running the store_data_to_sql.py script:
```python store_data_to_sql.py```