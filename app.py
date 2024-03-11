import streamlit as st
import pandas as pd
import plotly.express as px

df_vehicles = pd.read_csv('./vehicles_us.csv')

# Lines 7 to 57 are a shortened version of the preprocessing actions done in the EDA.ipynb file:
model_year_median = df_vehicles['model_year'].median()
df_vehicles['model_year'] = df_vehicles['model_year'].fillna(model_year_median)
df_vehicles['model_year'] = df_vehicles['model_year'].astype('int')

cylinders_median = df_vehicles['cylinders'].median()
df_vehicles['cylinders'] = df_vehicles['cylinders'].fillna(cylinders_median)
df_vehicles['cylinders'] = df_vehicles['cylinders'].astype('int')

odometer_median = df_vehicles['odometer'].median()
df_vehicles['odometer'] = df_vehicles['odometer'].fillna(odometer_median)
df_vehicles['odometer'] = df_vehicles['odometer'].astype('int')

df_vehicles['paint_color'] = df_vehicles['paint_color'].fillna('no color recorded')

df_vehicles['is_4wd'] = df_vehicles['is_4wd'].fillna(0.0)
df_vehicles['is_4wd'] = df_vehicles['is_4wd'].astype('bool')

def column_name_to_graph_name(column):
    if column == 'price':
        return 'Price'
    elif column == 'model_year':
        return 'Model Year'
    elif column == 'model':
        return 'Car Model'
    elif column == 'condition':
        return 'Condition'
    elif column == 'cylinders':
        return 'Cylinders'
    elif column == 'fuel':
        return 'Fuel'
    elif column == 'odometer':
        return 'Odometer'
    elif column == 'transmission':
        return 'Transmission'
    elif column == 'type':
        return 'Type of Car'
    elif column == 'paint_color':
        return 'Paint Color'
    elif column == 'is_4wd':
        return 'Four Wheel Drive?'
    elif column == 'date_posted':
        return 'Date Posted'
    elif column == 'days_listed':
        return 'Number of Days Listed'
    else:
        return 'Invalid Column Inputted'

for col in df_vehicles.columns:
    df_vehicles[column_name_to_graph_name(col)] = df_vehicles[col]
    df_vehicles = df_vehicles.drop(col, axis = 'columns')
df_first_table = df_vehicles

st.header('Welcome to the Vehicles App!')
st.write('This is a small test application for running and ' +
        'displaying EDA results for a Pandas DataFrame onto ' + 
        'local server with Streamlit and Plotly. Here is the '  +
        'dataset that we will be working with:')
factor1 = st.checkbox('Vehicles That Cost At Least $25,000 Only')
factor2 = st.checkbox('Vehicles Released in 2014 Only')
factor3 = st.checkbox('Vehicles Listed for More Than 100 Days Only')
factor4 = st.checkbox('No Manual and No Automatic Transmission')
if factor1:
    df_first_table = df_first_table[df_first_table['Price'] >= 25000]
if factor2:
    df_first_table = df_first_table[df_first_table['Model Year'] == 2014]
if factor3:
    df_first_table = df_first_table[df_first_table['Number of Days Listed'] >= 100]
if factor4:
    df_first_table = df_first_table[df_first_table['Transmission'] == 'other']
st.write(df_first_table)
count = len(df_first_table.index)
st.write('There are ' + str(count) + ' result(s) to show.')

st.header('Vehicle Histograms')
st.write('This first Plotly graph displays histograms for any applicable column ' + 
        'for the vehicles in the dataset (not including \"Four Wheel Drive?\" or \"Date Posted\"):')
applicable_columns = df_vehicles.columns.drop(['Four Wheel Drive?', 'Date Posted'])
histogram_col = st.selectbox(
    'Select a column to make a histogram from:',
    applicable_columns)
fig1 = px.histogram(df_vehicles, x=histogram_col)
fig1 = px.histogram(df_vehicles, x=histogram_col, 
                        title=histogram_col + ' Histogram')
fig1.update_layout(yaxis_title="Number of Vehicles") 
st.plotly_chart(fig1)

st.header('Vehicle Scatterplots: Price vs. Type over Different Model Years')
st.write('This second Plotly graph is a scatterplot comparing the price of different types of vehicles ' + 
        'over different model year releases. You can select whichever type of vehicle to display in the scatterplot ' + 
        'by clicking on a type in the legend:')
fig2 = px.scatter(
    df_vehicles,
    x="Model Year", 
    y="Price", 
    title='Price vs. Model Release Year for Different Types of Vehicles', 
    color="Type of Car",
)
st.plotly_chart(fig2)
st.write('We can see from this scatterplot that there was a spike in price for sedans, coupes, and convertibles around 1965. ' + 
        'Otherwise, the trends show a positive correlation between price and model year, regardless of the type of vehicle.')