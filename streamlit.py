import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from PIL import Image

# GLOBAL CONSTANTS
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
    
    # Ensure time columns are formatted as strings
    df['departing_time'] = df['departing_time'].astype(str)
    df['reaching_time'] = df['reaching_time'].astype(str)
    
    return df

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Data Dashboard"])

# Home page
if page == "Home":
    # Custom CSS for the home page
    st.markdown(
        """
        <style>
        .main {
            background-color: #f0f2f6;
            font-family: Arial, sans-serif;
        }
        .stTitle {
            color: #333;
            font-size: 36px;
            font-weight: bold;
            text-align: center;
            margin-top: 20px;
            margin-bottom: 10px;
        }
        .stLogo {
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            display: block;
            margin: 0 auto;
        }
        .stDescription {
            color: #555;
            line-height: 1.6;
            margin: 0 auto;
            max-width: 900px;
            text-align: center;
        }
        .stSection {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            margin-bottom: 20px;
        }
        .stButton>button {
            color: white;
            background-color: #ff4b4b;
            border-radius: 10px;
            font-size: 16px;
            border: none;
            padding: 10px 20px;
        }
        .stButton>button:hover {
            background-color: #ff7878;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown('<h1 class="stTitle">Exploring Redbus Data with Advanced Scraping and Filtering</h1>', unsafe_allow_html=True)

    # Display the logo image
    logo_url = "https://s3.rdbuz.com/Images/rdc/rdc-redbus-logo.svg"
    st.image(logo_url, width=300, caption="Redbus Logo", use_column_width=False)

    st.markdown(
        """
        <div class="stDescription">
        <div class="stSection">
            <h2>Project Overview</h2>
            <p>Welcome to the "Redbus Data Scraping and Filtering Project"! The project utilizes selenium to automate the extraction of comprehensive bus travel data from Redbus, including routes, schedules, and availability. Our goal is to enhance the transportation sector by offering a dynamic tool that simplifies data collection and analysis, helping stakeholders make informed decisions and improve operational strategies.</p>
        </div>

        <div class="stSection">
            <h2>Key Business Applications</h2>
            <p>This project has the potential to transform various aspects of the transportation industry:</p>
            <ul>
                <li><strong>Travel Aggregators:</strong> Provide up-to-date bus schedules and seat availability to enhance customer service.</li>
                <li><strong>Market Analysis:</strong> Analyze travel trends and consumer preferences for better market insights.</li>
                <li><strong>Customer Experience:</strong> Offer tailored travel options and improved services based on data insights.</li>
                <li><strong>Competitive Intelligence:</strong> Compare service offerings and pricing with competitors for strategic advantage.</li>
            </ul>
        </div>

        <div class="stSection">
            <h2>Project Approach</h2>
            <h3>Data Extraction:</h3>
            <p>Utilize Selenium to systematically scrape data from Redbus, capturing essential details like routes, schedules, and prices.</p>
            <h3>Data Storage:</h3>
            <p>Organize and store the extracted information in a structured SQL database for easy access and management.</p>
            <h3>Interactive Dashboard:</h3>
            <p>Develop an intuitive Streamlit application to visualize and filter the data. Users can explore various filters, including bus type, route, price range, and ratings.</p>
            <h3>Data Analysis:</h3>
            <p>Enable sophisticated data analysis and filtering through SQL queries integrated into the Streamlit app, providing users with actionable insights.</p>
        </div>

        <div class="stSection">
            <h2>Expected Outcomes</h2>
            <ul>
                <li>Efficiently scrape data for at least 10 state transport services and private buses from Redbus.</li>
                <li>Organize the data in a SQL database, ensuring a clear and efficient structure.</li>
                <li>Build a user-friendly Streamlit app for filtering and analyzing bus travel data.</li>
                <li>Deliver an application that is both effective and easy to navigate.</li>
            </ul>
        </div>

        <div class="stSection">
            <h2>Success Criteria</h2>
            <ul>
                <li>Accuracy of scraped data and its completeness.</li>
                <li>Design and efficiency of the database schema.</li>
                <li>User experience and functionality of the Streamlit application.</li>
                <li>Responsiveness and effectiveness of the filtering options.</li>
                <li>Overall code quality and adherence to best practices.</li>
            </ul>
        </div>

        <div class="stSection">
            <h2>Skills Acquired</h2>
            <ul>
                <li>Web Scraping with Selenium</li>
                <li>Data Management with SQL</li>
                <li>Interactive Data Visualization using Streamlit</li>
                <li>Python Programming for Data Analysis</li>
            </ul>
        </div>

        <div class="stSection">
            <h2>Project Domain</h2>
            <p>Transportation</p>
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="text-align: center;">
            <a href="#Data Dashboard" class="stButton">Explore the Data Dashboard</a>
        </div>
        """,
        unsafe_allow_html=True
    )

# Data Dashboard page
if page == "Data Dashboard":
    # App Title
    st.title("🚌 Redbus Data Dashboard")

    # Custom CSS for styling
    st.markdown(
        """
        <style>
        .main {
            background-color: #f0f2f6;
        }
        .stButton>button {
            color: white;
            background-color: #ff4b4b;
            border-radius: 10px;
            font-size: 16px;
        }
        .stButton>button:hover {
            background-color: #ff7878;
        }
        .css-1d391kg {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 10px;
        }
        .css-1v3fvcr {
            border-radius: 10px;
            overflow: hidden;
            background-color: #ffffff;
            padding: 10px;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
        }
        .css-1b1x5wm {
            color: #333;
        }
        .stSidebar .css-1d391kg {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Connect to the database and load the data
    engine = connect_to_db()
    data = load_data(engine)

    # Sidebar for filters
    st.sidebar.header("🔍 Filters")

    # State filter
    states = data['state'].unique()
    selected_state = st.sidebar.selectbox("Select State", options=["All"] + list(states), key='state_filter')

    # Filter data based on selected state
    if selected_state != "All":
        data = data[data['state'] == selected_state]
        
    # Update Bus Name filter options based on the filtered data
    bus_names = data['bus_name'].unique()
    selected_bus_name = st.sidebar.selectbox("Select Bus Name", options=["All"] + list(bus_names), key='bus_filter')

    # Price filter
    min_price, max_price = float(data['price'].min()), float(data['price'].max())
    price_range = st.sidebar.slider("Select Price Range", min_value=min_price, max_value=max_price, value=(min_price, max_price), key='price_filter')

    # Rating filter
    min_rating, max_rating = float(data['star_rating'].min()), float(data['star_rating'].max())
    rating_range = st.sidebar.slider("Select Star Rating Range", min_value=min_rating, max_value=max_rating, value=(min_rating, max_rating), key='rating_filter')

    # Filter the data based on user input
    if selected_state != "All":
        data = data[data['state'] == selected_state]
    if selected_bus_name != "All":
        data = data[data['bus_name'] == selected_bus_name]
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
