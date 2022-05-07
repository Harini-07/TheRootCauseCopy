import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from fbprophet.plot import plot_plotly, plot_components_plotly
import plotly.offline as py
from fbprophet.plot import add_changepoints_to_plot
import streamlit as st
from prophet import Prophet



DistrictWise2014 = pd.read_csv("DataSet/01_District_wise_crimes_committed_IPC_2014.csv")
 
def CrimesAgainstWomenComparison(state1,district1,state2,district2):
    global DistrictWise2014
    crimeAgainstWomeColumns = ['States/UTs', 'District', 'Year', 'Rape', 'Custodial Rape',
    'Custodial_Gang Rape', 'Custodial_Other Rape',
    'Rape other than Custodial', 'Rape_Gang Rape', 'Rape_Others',
    'Attempt to commit Rape', 'Kidnapping & Abduction_Total',
    'Kidnapping & Abduction', 'Kidnapping & Abduction in order to Murder',
    'Kidnapping for Ransom',
    'Kidnapping & Abduction of Women to compel her for marriage',
    'Other Kidnapping', 'Acid attack', 'Attempt to Acid Attack',
    'Dowry Deaths', 'Assault on Women with intent to outrage her Modesty',
    'Sexual Harassment',
    'Assault or use of criminal force to women with intent to Disrobe',
    'Voyeurism', 'Stalking', 'Other Assault on Women',
    'Insult to the Modesty of Women', 'At Office premises',
    'Other places related to work', 'In Public Transport system',
    'Places other than 231, 232 & 233',
    'Cruelty by Husband or his Relatives',
    'Importation of Girls from Foreign Country',
    'HumanTrafficking']

    crimeAgainstWomen = DistrictWise2014[crimeAgainstWomeColumns]
    crimeAgainstWomen["TotalCrimes"] = crimeAgainstWomen[list(crimeAgainstWomen.columns)[3::]].sum(axis=1)

    
    columns = crimeAgainstWomen.columns[3:-2]
    CrimesAgainstWomen = pd.DataFrame(columns = crimeAgainstWomen.columns)
    CrimesAgainstWomen = CrimesAgainstWomen.append(crimeAgainstWomen[(crimeAgainstWomen["States/UTs"] == state1) & (crimeAgainstWomen["District"] == district1)],ignore_index = True)
    CrimesAgainstWomen = CrimesAgainstWomen.append(crimeAgainstWomen[(crimeAgainstWomen["States/UTs"] == state2) & (crimeAgainstWomen["District"] == district2)],ignore_index=True)

    mostCommonCrimesAgainstWomen = CrimesAgainstWomen[columns].sort_values(by=1,axis=1,ascending=False).iloc[:,:20]
    mostCommonCrimesAgainstWomen.insert(loc=0, column="States/UTs", value=CrimesAgainstWomen["States/UTs"])
    mostCommonCrimesAgainstWomen.insert(loc=1, column="District", value=CrimesAgainstWomen["District"])

    y_axis1 = mostCommonCrimesAgainstWomen[mostCommonCrimesAgainstWomen["District"]==district1].to_numpy().tolist()[0][2:]
    y_axis2 = mostCommonCrimesAgainstWomen[mostCommonCrimesAgainstWomen["District"]==district2].to_numpy().tolist()[0][2:]
    fig = go.Figure(data=[
        go.Bar(name=district1, x=mostCommonCrimesAgainstWomen.columns[2:],y = y_axis1),
        go.Bar(name=district2, x=mostCommonCrimesAgainstWomen.columns[2:],y = y_axis2)
    ])
    fig.update_layout(barmode='group')
    return fig


def CrimeComparison(state1,district1,state2,district2):
    Crimes = DistrictWise2014.copy()
    Crimes1 = pd.DataFrame()
    Crimes1 = Crimes1.append(Crimes[(Crimes["States/UTs"] == state1) & (Crimes["District"] == district1)],ignore_index = True)
    Crimes1 = Crimes1.append(Crimes[(Crimes["States/UTs"] == state2) & (Crimes["District"] == district2)],ignore_index=True)

    columns = DistrictWise2014.columns[3:]

    mostCommonCrimes = Crimes1[columns].sort_values(by=1,axis=1,ascending=False).iloc[:,:15]
    mostCommonCrimes.insert(loc=0, column="States/UTs", value=Crimes1["States/UTs"])
    mostCommonCrimes.insert(loc=1, column="District", value=Crimes1["District"])

    y_axis1 = mostCommonCrimes[mostCommonCrimes["District"]==district1].to_numpy().tolist()[0][2:]
    y_axis2 = mostCommonCrimes[mostCommonCrimes["District"]==district2].to_numpy().tolist()[0][2:]
    fig1 = go.Figure(data=[
        go.Bar(name=district1, x=mostCommonCrimes.columns[2:],y = y_axis1),
        go.Bar(name=district2, x=mostCommonCrimes.columns[2:],y = y_axis2)
    ])
    fig1.update_layout(barmode='group')
    return fig1
    