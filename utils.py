import streamlit as st
import base64
import streamlit.components.v1 as components

from PATHS import NAVBAR_PATHS


def inject_custom_css():
    with open('assets/bootstrap.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def get_current_route():
    try:
        return st.experimental_get_query_params()['nav'][0]
    except:
        return None


def navbar_component():
    navbar_items = []
    for key, value in NAVBAR_PATHS.items():
        navbar_items.append(f'<a class="nav-link" role="button" target="_self" href="/?nav={value}">{key}</a>')

    component = rf'''
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <a class="navbar-brand" href="/?nav=home" target="_self">
                <img src="https://i.pinimg.com/736x/31/3e/81/313e819720ceb82cf4e7115bb274b09c.jpg" width="75" height="75" class="d-inline-block align-top" alt="" style="object-fit: scale-down; text-align: justify; margin: auto; float: left;">
            </a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav mr-auto">
                    <li class="nav-item active">
                        {navbar_items[0]}
                    </li>
                    <li class="nav-item active">
                        {navbar_items[1]}
                    </li>
                    <li class="nav-item active">
                        {navbar_items[2]}
                    </li>
                    <li class="nav-item active">
                        {navbar_items[3]}
                    </li>
                    <li class="nav-item active">
                        {navbar_items[4]}
                    </li>
                    <li class="nav-item active">
                        {navbar_items[5]}
                    </li>
            </div>
        </nav>
    '''

    st.markdown(component, unsafe_allow_html=True)