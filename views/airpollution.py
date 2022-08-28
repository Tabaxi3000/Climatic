import streamlit as st
import plotly.express as px
import pandas as pd


# Function to get any data from a URL into a Pandas dataframe
@st.cache
def get_data(url):
    return pd.read_csv(url)


# Getting the CO2 data
@st.cache
def get_air_pollution_data(): 
    # OWID Data on CO2 and Greenhouse Gas Emissions
    # Creative Commons BY license
    url = 'https://raw.githubusercontent.com/owid/owid-datasets/master/datasets/Air%20pollution%20emissions%20(CEDS%2C%202022)/Air%20pollution%20emissions%20(CEDS%2C%202022).csv'
    return get_data(url)

def load_view():

    # Dataframe with CO2 data
    df_air_pollution = get_air_pollution_data()


    # Text at top of website page using markdown notation (like README.md)
    st.markdown("""
    # World Air Pollutant Emissions (CO and SO2)
    The graphs below show the CO (carbon monoxide) and SO2 (sulfure dioxide) per capita (in tons)
    for different countries / continents.
    __Hover over any of the charts to see more detail.__
    Data comes from here: https://github.com/owid/owid-datasets/tree/master/datasets/Air%20pollution%20emissions%20(CEDS%2C%202022)
    """)

    # Setting up some columns with spacing
    col2, space2, col3 = st.columns((10,1,10))

    # Populating first column
    with col2:

        # List of default countries
        default_countries = ['United States','United Kingdom', 'China', 'Australia']

        # Getting all unique countries
        countries = df_air_pollution['Entity'].unique()

        # Dropdown menu that also allows for text input
        selected_countries = st.multiselect('Select country or continent',countries,default_countries)

        # Getting a smaller dataframe with only the countries selected
        df3 = df_air_pollution.query('Entity in @selected_countries' )

        # Plotly line graph
        fig2 = px.line(df3,"Year","co_per_capita",color="Entity")

        st.plotly_chart(fig2, use_container_width=True)

    # Populating next column
    with col3:
        # List of default countries
        default_countries = ['United States','United Kingdom', 'China', 'Australia', 'France']

        # Getting all unique countries
        countries = df_air_pollution['Entity'].unique()

        # Dropdown menu that also allows for text input
        selected_countries_2 = st.multiselect('Select country or continent',countries,default_countries)

        # Getting a smaller dataframe with only the countries selected
        df4 = df_air_pollution.query('Entity in @selected_countries_2' )

        # Plotly line graph
        fig3 = px.line(df4,"Year","so2_per_capita",color="Entity")

        st.plotly_chart(fig3, use_container_width=True)
        