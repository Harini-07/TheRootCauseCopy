import TheRootCauseApp1
import TheRootCauseApp2
import streamlit as st
# import PathFinder.pathFinder as pathFinder


PAGES = {
    "Crime Visualization": TheRootCauseApp1,
    "Travel Comparison": TheRootCauseApp2,
    # "Path Finder": pathFinder
}


st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()