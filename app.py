import streamlit as st
import utils as utl
from views import home, co2, airpollution, wildfires, donate

st.set_page_config(layout="wide", page_title='Climatic', page_icon="./assets/climatic-logo.jpg")
st.set_option('deprecation.showPyplotGlobalUse', False)
utl.inject_custom_css()
utl.navbar_component()

def navigation():
    route = utl.get_current_route()
    if route == "home":
        home.load_view()
    elif route == "co2":
        co2.load_view()
    elif route == "airpollution":
        airpollution.load_view()
    elif route == "wildfires":
        wildfires.load_view()
    elif route == "donate":
        donate.load_view()
    elif route == None:
        home.load_view()
        
navigation()