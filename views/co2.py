import streamlit as st
import plotly.express as px
import plotly
import pandas as pd


# Function to get any data from a URL into a Pandas dataframe
@st.cache
def get_data(url):
    return pd.read_csv(url)


# Getting the CO2 data
@st.cache
def get_co2_data(): 
    # OWID Data on CO2 and Greenhouse Gas Emissions
    # Creative Commons BY license
    url = 'https://github.com/owid/co2-data/raw/master/owid-co2-data.csv'
    return get_data(url)

def load_view():

    # Dataframe with CO2 data
    df_co2= get_co2_data()


    # Text at top of website page using markdown notation (like README.md)
    st.markdown("""
    # World CO2 emissions
    The graph below shows the CO2 emissions per capita (in tons) for the entire 
    world and individual countries over time.
    Select a year with the slider in the left-hand graph and countries / continents 
    from the drop down menu in the other one.
    Scroll down to see a chart demonstrating the rise in global CO2 levels.
    Hover over any of the charts to see more detail.
    Data comes from here: https://github.com/owid/co2-data
    """)

    # Setting up some columns with spacing
    col2, space2, col3 = st.columns((10,1,10))

    # Populating first column
    with col2:

        # Slider to select the year
        year = st.slider('Select year',1750,2020)

        # Choropleth map (world heatmap) using plotly library, where passing in year from slider to graph
        fig = px.choropleth(df_co2[df_co2['year']==year], locations="iso_code",
                            color="co2_per_capita",
                            hover_name="country",
                            range_color=(0,25),
                            color_continuous_scale=plotly.colors.sequential.YlOrBr)

        # Passing the graph to Streamlit plotly_chart function so it will appear on screen
        st.plotly_chart(fig, use_container_width=True)

    # Populating next column
    with col3: 

        # List of default countries
        default_countries = ['World','United States','United Kingdom','EU-27','China', 'Australia']

        # Getting all unique countries
        countries = df_co2['country'].unique()

        # Dropdown menu that also allows for text input
        selected_countries = st.multiselect('Select country or continent',countries,default_countries)

        # Getting a smaller dataframe with only the countries selected
        df3 = df_co2.query('country in @selected_countries' )

        # Plotly line graph
        fig2 = px.line(df3,"year","co2_per_capita",color="country")

        st.plotly_chart(fig2, use_container_width=True)

    col4, space3, col5,space4,col6 = st.columns((10,1,10,1,10))

    with col4:
        st.markdown("""
        This  graph shows the rise in total CO2 emissions since 1850, with a sharp rise in 
        emissions mid-twentieth century.
        """)

    with col5:
        st.subheader("Total world CO2 emissions")
        fig4 = px.line(df3.query("country == 'World' and year >= 1850"),"year","co2")
        st.plotly_chart(fig4, use_container_width=True)