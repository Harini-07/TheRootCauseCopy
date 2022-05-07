#Comparison

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from CrimeComparisons import CrimesAgainstWomenComparison,CrimeComparison

DistrictWise2014 = pd.read_csv("DataSet/01_District_wise_crimes_committed_IPC_2014.csv")

def app():
    
    states1 = sorted(list(set(DistrictWise2014["States/UTs"])))
    state1 = st.selectbox("From State: ",states1)
    districts1 = sorted(list(set(DistrictWise2014[DistrictWise2014["States/UTs"]==state1]["District"])))
    district1 = st.selectbox("From District: ",districts1)

    states2 = sorted(list(set(DistrictWise2014["States/UTs"])))
    state2 = st.selectbox("To State: ",states2)
    districts2 = sorted(list(set(DistrictWise2014[DistrictWise2014["States/UTs"]==state2]["District"])))
    district2 = st.selectbox("To District: ",districts2)

    g = ("MALE","FEMALE")
    gender = st.radio("Gender: ",g)

    if gender == "FEMALE":
        st.plotly_chart(CrimesAgainstWomenComparison(state1,district1,state2,district2))
        st.plotly_chart(CrimeComparison(state1,district1,state2,district2))
    else:
        st.plotly_chart(CrimeComparison(state1,district1,state2,district2))
