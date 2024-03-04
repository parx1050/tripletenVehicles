import streamlit as st
import pandas as pd
import plotly.express as px

df_vehicles = pd.read_csv('./vehicles_us.csv')

st.header('Welcome to the Vehicles App!', divider = 'rainbow')
st.write('This is a small test application for running and ' +
        'displaying EDA results for a Pandas DataFrame onto ' + 
        'local server with Streamlit and Plotly. Here is the '  +
        'dataset that we will be working with:')
st.write(df_vehicles)
st.write('\n\n\n')

df_vehicles.info()
df_vehicles.head()