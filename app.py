import streamlit as st
import pandas as pd
import plotly.express as px

df_vehicles = pd.read_csv('./vehicles_us.csv')

st.header('Welcome to the Vehicles App!')
st.write('This is a small test application for running and ' +
        'displaying EDA results for a Pandas DataFrame onto ' + 
        'local server with Streamlit and Plotly. Here is the '  +
        'dataset that we will be working with:')
factor1 = st.checkbox('Vehicles That Cost At Least $100,000 Only')
factor2 = st.checkbox('Vehicles Released in 2014 Only')
factor3 = st.checkbox('Vehicles Listed for More Than 100 Days Only')
factor4 = st.checkbox('Manual Transmission Only')
if factor1:
    df_vehicles = df_vehicles[df_vehicles['price'] >= 100000]
if factor2:
    df_vehicles = df_vehicles[df_vehicles['model_year'] == 2014]
if factor3:
    df_vehicles = df_vehicles[df_vehicles['days_listed'] >= 100]
if factor4:
    df_vehicles = df_vehicles[df_vehicles['transmission'] == 'manual']
st.write(df_vehicles)
count = len(df_vehicles.index)
st.write('There are ' + str(count) + ' result(s) to show.')

st.header('Vehicle Histograms')
st.write('This first Plotly graph displays histograms for any applicable column ' + 
        'for the vehicles in the dataset (not including \"is_4wd\" or \"date_posted\"):')
applicable_columns = df_vehicles.columns.drop(['is_4wd', 'date_posted'])
histogram_col = st.selectbox(
    'Select a column to make a histogram from:',
    applicable_columns)
fig1 = px.histogram(df_vehicles, x=histogram_col)
st.plotly_chart(fig1)

st.header('Vehicle Scatterplots: Price vs. Type over Different Model Years')
st.write('This second Plotly graph is a scatterplot comparing the price of different types of vehicles ' + 
        'over different model year releases. You can select whichever type of vehicle to display in the scatterplot ' + 
        'by clicking on a type in the legend:')
fig2 = px.scatter(
    df_vehicles,
    x="model_year", 
    y="price", 
    labels=['Model Year', 'Price'], 
    color="type",
)
st.plotly_chart(fig2)
st.write('We can see from this scatterplot that there was a spike in price for sedans, coupes, and convertibles around 1965. ' + 
        'Otherwise, the trends show a positive correlation between price and model year, regardless of the type of vehicle.')