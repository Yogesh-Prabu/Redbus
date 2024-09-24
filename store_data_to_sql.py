import mysql.connector
import pandas as pd

# CONSTANTS
database_name = 'project_redbus'
table_name = 'bus_routes'
csv_path = '03_cleaned_data.csv'

# SQL QUERY --------------------------------START-------------------------------------------------------------
# CREATE DATABASE
create_db_query = """CREATE DATABASE IF NOT EXISTS PROJECT_REDBUS"""

# CREATE TABLE
create_table_query = """CREATE TABLE IF NOT EXISTS bus_routes (
id INT AUTO_INCREMENT PRIMARY KEY,
state TEXT NOT NULL,
route_name TEXT NOT NULL,
route_link TEXT NOT NULL,
bus_name TEXT NOT NULL,
bus_type TEXT NOT NULL,
departing_time TIME NOT NULL,
duration TEXT NOT NULL,
reaching_time TIME NOT NULL,
price DECIMAL(10, 2) NOT NULL,
star_rating FLOAT NOT NULL,
seats_available INT NOT NULL)"""

# TRUNCATE TABLE
truncate_table_query = f"TRUNCATE TABLE {table_name}"

# INSERT DATA INTO TABLE
insert_data_into_table_query = """INSERT INTO bus_routes (state,route_name,route_link,bus_name,bus_type,departing_time,duration,reaching_time,price,star_rating,seats_available) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
ON DUPLICATE KEY UPDATE
state = VALUES(state),
route_name = VALUES(route_name),
route_link = VALUES(route_link),
bus_name = VALUES(bus_name),
bus_type = VALUES(bus_type),
departing_time = VALUES(departing_time),
duration = VALUES(duration),
reaching_time = VALUES(reaching_time),
price = VALUES(price),
star_rating = VALUES(star_rating),
seats_available = VALUES(seats_available)
"""
# SQL QUERY --------------------------------------END---------------------------------------------------------

def read_data_in_chunks(csv_path, chunks=1000):
    return pd.read_csv(csv_path, chunksize=chunks)

def insert_data_to_sql(cursor, insert_data_into_table_query, chunk):
    cursor.executemany(insert_data_into_table_query, chunk)

def disable_indexes_and_keys(cursor, table_name, enabled=True):
    if enabled:
        cursor.execute(f'ALTER TABLE {table_name} ENABLE KEYS')
        print(f"Keys and indexes enabled on table {table_name}")
    else:
        cursor.execute(f"ALTER TABLE {table_name} DISABLE KEYS")
        print(f"Keys and indexes disabled on table {table_name}")

# Create connection to SQL database
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )
    if db.is_connected():
        print("Database connected successfully!")
        cursor = db.cursor(buffered=True)

        # Create database
        cursor.execute(create_db_query)
        
        # Select created database
        db.database = database_name

        # Create table
        cursor.execute(create_table_query)

        # Truncate table before inserting data
        cursor.execute(truncate_table_query)
        print(f"Table {table_name} truncated successfully!")

        # Disable indexes and keys for performance
        disable_indexes_and_keys(cursor, table_name, enabled=False)

        # Read data in chunks and insert into table
        chunk_data = read_data_in_chunks(csv_path)


        for chunk in chunk_data:
            data_tuple = [tuple(row) for row in chunk.values]
            insert_data_to_sql(cursor, insert_data_into_table_query, data_tuple)
            db.commit()  # Commit each chunk
        print("Data inserted successfully!")

        # Enable indexes and keys
        disable_indexes_and_keys(cursor, table_name, enabled=True)

    else:
        print("Failed to connect to the database")

except mysql.connector.Error as err:
    print(f"Error connecting to Database: {err}")

finally:
    # Close cursor and database connection
    if db.is_connected():
        cursor.close()
        db.close()
        print("Database connection closed.")
