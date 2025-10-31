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

with st.sidebar:
  st.header("input features")
  island = st.selectbox(
      "island",
    ("Bisco","Dream","Torgersen"))
  sex = st.selectbox("Gender",("male","female"))
  bill_length_mm = st.slider("bill lenght in mm", df.bill_length_mm.min(),df.bill_length_mm.max(),df.bill_length_mm.mean())
  bill_depth_mm = st.slider("bill depth in mm", df.bill_depth_mm.min(),df.bill_depth_mm.max(),df.bill_depth_mm.mean())
  flipper_length_mm = st.slider("flipper lenght in mm", df.flipper_length_mm.min(),df.flipper_length_mm.max(),df.flipper_length_mm.mean())
  body_mass_g = st.slider("body mass in g", int(df.body_mass_g.min()),int(df.body_mass_g.max()),float(df.body_mass_g.mean()))


