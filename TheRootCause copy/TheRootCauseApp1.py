import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from prophet import Prophet
from datetime import datetime
from fbprophet.plot import plot_plotly, plot_components_plotly
import plotly.offline as py
from fbprophet.plot import add_changepoints_to_plot



DW2002_2012 = pd.read_csv("DataSet/01_District_wise_crimes_committed_IPC_2001_2012.csv")
DistrictWise2014 = pd.read_csv("DataSet/01_District_wise_crimes_committed_IPC_2014.csv")
DistrictWise2013 = pd.read_csv("DataSet/01_District_wise_crimes_committed_IPC_2013.csv")

def app():
  def Crimes20022012(state,district,crime):
    global DW2002_2012
    districtWise = DW2002_2012[(DW2002_2012["STATE/UT"] == state) & (DW2002_2012["DISTRICT"] == district)]
    fig = px.line(districtWise,x = "YEAR",y = crime)
    return fig

  def ForecastCrime(state,district,crime):
    global DW2002_2012
    districtWise = DW2002_2012[(DW2002_2012["STATE/UT"] == state) & (DW2002_2012["DISTRICT"] == district)]
    District_wise_crime = districtWise[["YEAR",crime]]
    District_wise_crime.rename(columns = {'YEAR':'ds', crime:'y'}, inplace = True)
    District_wise_crime["ds"]=District_wise_crime.apply(lambda x:datetime.strptime(str(x["ds"]), '%Y'),axis=1)
    m = Prophet()
    m.fit(District_wise_crime)
    future = m.make_future_dataframe(periods=5,freq="Y")
    # print(District_wise_crime)
    # print(future.tail())
    forecast = m.predict(future)
    print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper',"trend"]].tail())
    if forecast["yhat"].is_monotonic == True:
      st.write(f"The crimes are increasing.It is less safe to travel to {district}")
    else:
      st.write(f"The crime is decreasing.It is safe to travel to {district}")
    fig = plot_plotly(m, forecast)
    return fig



  
  states = sorted(list(set(DW2002_2012["STATE/UT"])))
  state = st.selectbox("States: ",states)

  districts = sorted(list(set(DW2002_2012[DW2002_2012["STATE/UT"]==state]["DISTRICT"])))
  district = st.selectbox("District: ",districts)

  crimes = DW2002_2012.columns[3:]
  crime = st.selectbox("Crime: ",crimes)
  ForecastCrime(state,district,crime)
  st.plotly_chart(Crimes20022012(state,district,crime))
  st.plotly_chart(ForecastCrime(state,district,crime))