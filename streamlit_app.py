import pandas as pd 
import streamlit as st

st.title('ML visualization app')

st.write('Penguin Species prediction model')
with st.expander("Data"):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df

  st.write('**X-all-values-from-dataset**')
  X = df.drop('species', axis=1)
  X

  st.write('**y-unique-values**')
  y = df.species.unique()
  y

with st.expander('Data visualization'):
  st.write('scatter-plot')
  st.scatter_chart(data=df,x="bill_length_mm",y="body_mass_g",color='species')
