import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Variables
database_name = 'project_redbus'
table_name = 'bus_routes'

# Connect to the database using SQLAlchemy
def connect_to_db():
    connection_string = f"mysql+mysqlconnector://root:@localhost/{database_name}"
    engine = create_engine(connection_string)
    return engine

# Load data from the database
def load_data(engine):
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query, engine)
    
    # Convert timedelta to hours and minutes
    df['departing_time'] = df['departing_time'].apply(lambda x: f"{x.components.hours:02}:{x.components.minutes:02}")
    df['reaching_time'] = df['reaching_time'].apply(lambda x: f"{x.components.hours:02}:{x.components.minutes:02}")
    
    return df

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Data Dashboard"])

# Home page
if page == "Home":
    st.title("Exploring Redbus Data with Advanced Scraping and Filtering")

    # Display the logo image
    logo_url = "https://s3.rdbuz.com/Images/rdc/rdc-redbus-logo.svg"
    st.image(logo_url, width=300, caption="Redbus Logo", use_column_width=False)

    st.markdown(
        """
        ## Project Overview
        Welcome to the "Redbus Data Scraping and Filtering Project"! This project uses Selenium to automate data extraction from Redbus, including routes, schedules, and availability.
        
        ## Key Business Applications
        - **Travel Aggregators:** Enhance customer service with up-to-date bus schedules and seat availability.
        - **Market Analysis:** Gain insights into travel trends and consumer preferences.
        - **Customer Experience:** Offer tailored travel options and improved services based on data insights.
        - **Competitive Intelligence:** Compare service offerings and pricing with competitors for strategic advantage.
        
        ## Project Approach
        - **Data Extraction:** Use Selenium to scrape data from Redbus.
        - **Data Storage:** Store the data in a SQL database.
        - **Interactive Dashboard:** Visualize and filter the data using a Streamlit application.
        - **Data Analysis:** Provide actionable insights through SQL queries in the Streamlit app.

        ## Expected Outcomes
        - Scrape data for multiple state transport services and private buses from Redbus.
        - Organize the data in a SQL database.
        - Build a user-friendly Streamlit app for data filtering and analysis.
        
        ## Skills Acquired
        - Web Scraping with Selenium
        - Data Management with SQL
        - Interactive Data Visualization using Streamlit
        - Python Programming for Data Analysis
        """,
        unsafe_allow_html=True
    )

# Data Dashboard page
if page == "Data Dashboard":
    st.title("🚌 Redbus Data Dashboard")

    # Connect to the database and load the data
    engine = connect_to_db()
    data = load_data(engine)

    # Sidebar for filters
    st.sidebar.header("🔍 Filters")

    # State name dropdown
    states = data['state'].unique()
    selected_state = st.sidebar.selectbox("Select State", options=["All"] + list(states))

    # Bus Name dropdown
    bus_names = data['bus_name'].unique()
    selected_bus_name = st.sidebar.selectbox("Select Bus Name", options=["All"] + list(bus_names))

    # Route Name filter, dependent on the selected state
    if selected_state == "All":
        route_names = data['route_name'].unique()
    else:
        route_names = data[data['state'] == selected_state]['route_name'].unique()
        
    selected_route_name = st.sidebar.selectbox("Select Route Name", options=["All"] + list(route_names))

    # Price slider
    min_price, max_price = float(data['price'].min()), float(data['price'].max())
    price_range = st.sidebar.slider("Select Price Range", min_value=min_price, max_value=max_price, value=(min_price, max_price))

    # Rating slider
    min_rating, max_rating = float(data['star_rating'].min()), float(data['star_rating'].max())
    rating_range = st.sidebar.slider("Select Star Rating Range", min_value=min_rating, max_value=max_rating, value=(min_rating, max_rating))

    # Filter the data based on user input
    if selected_state != "All":
        data = data[data['state'] == selected_state]
    if selected_bus_name != "All":
        data = data[data['bus_name'] == selected_bus_name]
    if selected_route_name != "All":
        data = data[data['route_name'] == selected_route_name]
        
    data = data[(data['price'] >= price_range[0]) & (data['price'] <= price_range[1])]
    data = data[(data['star_rating'] >= rating_range[0]) & (data['star_rating'] <= rating_range[1])]

    # Show the filtered data
    st.dataframe(data)

    # Download button
    st.download_button(
        label="Download Data as CSV",
        data=data.to_csv(index=False),
        file_name='filtered_redbus_data.csv',
        mime='text/csv'
    )
