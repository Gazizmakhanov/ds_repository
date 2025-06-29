import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')
st.header('Welcome to my first app on render!')
fig = px.scatter(df, x='price', y='model_year')
st.plotly_chart(fig)

fig = px.histogram(df, x='cylinders', nbins=6, title='Histogram of Values')
st.plotly_chart(fig, use_container_width=True)

use_more_bins = st.checkbox("Use more bins", value=False)

nbins = 15 if use_more_bins else 5
fig = px.histogram(df, x='cylinders', nbins=nbins, title=f'Histogram with {nbins} Bins')
st.plotly_chart(fig, use_container_width=True)