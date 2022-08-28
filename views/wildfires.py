import streamlit as st
import plotly.express as px
import pandas as pd


# Function to get any data from a URL into a Pandas dataframe
@st.cache
def get_data(url):
    return pd.read_csv(url)


# Getting the CO2 data
@st.cache
def get_wildfire_data(): 
    # OWID Data on CO2 and Greenhouse Gas Emissions
    # Creative Commons BY license
    url = 'https://raw.githubusercontent.com/owid/owid-datasets/master/datasets/Wildfire%20data%20in%20the%20US%20(NIFC)/Wildfire%20data%20in%20the%20US%20(NIFC).csv'
    return get_data(url)

def load_view():

    # Dataframe with CO2 data
    df_wildfire = get_wildfire_data()


    # Text at top of website page using markdown notation (like README.md)
    st.markdown("""
    # United States Wildfires Data
    The graphs below show the number of wildfires and annual acres burned from 1926 to 2017.
    __Hover over any of the charts to see more detail.__
    Data comes from here: https://github.com/owid/owid-datasets/tree/master/datasets/Wildfire%20data%20in%20the%20US%20(NIFC)
    """)

    # Setting up some columns with spacing
    col2, space2, col3 = st.columns((10,1,10))

    # Populating first column
    with col2:
        st.subheader("Annual United States Wildfires")
        # Plotly line graph
        fig2 = px.line(df_wildfire,"Year","Number of wildfires - full series (NIFC)",color="Entity")

        st.plotly_chart(fig2, use_container_width=True)

    # Populating next column
    with col3:
        
        st.subheader("Annual United States Acres Burned")
        # Plotly line graph
        fig2 = px.line(df_wildfire,"Year","Acres burned - full series (NIFC)",color="Entity")

        st.plotly_chart(fig2, use_container_width=True)
        