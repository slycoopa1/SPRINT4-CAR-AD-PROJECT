import pandas as pd 
import numpy as np
import plotly.express as px
import streamlit as st

df = pd.read_csv('vehicles_us.csv')

df['price'] = pd.to_numeric(df['price'], errors='coerce')
df['price'].fillna(0, inplace=True)

st.header('Old cars are cooler than new cars')
st.write('They used to have personality')

st.title('Car Sales Dashboard')

if st.checkbox('Show Raw Data'):
    st.write(df)

column = st.selectbox(
    'Select a column to view its distribution',
    options=['price', 'odometer', 'model_year']
)

if column:
    fig = px.histogram(df, x=column)
    st.plotly_chart(fig)

fig = px.histogram(df, x='price', nbins=20)
st.plotly_chart(fig)

scatter = px.scatter(df, x='model_year', y='price')
st.plotly_chart(scatter)
