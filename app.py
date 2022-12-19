import numpy as np
import pandas as pd
import streamlit as st
import pickle
modal = pickle.load(open("RidgeModel.pkl", "rb"))


df = pd.read_csv("practo_cleandata.csv")
st.title("Doctor Fee Prediction")

for column in df.columns:
  print(df[column].value_counts())
  print("-"*20)

degree_count = df['Degree'].value_counts()
degree_count_less_10 = degree_count[degree_count <=10]
df['Degree'] = df['Degree'].apply(lambda x: 'other' if x in degree_count_less_10 else x)

Location_count = df['Location'].value_counts()
Location_count_less_10 = Location_count[Location_count <=10]
df['Location'] = df['Location'].apply(lambda x: 'other' if x in Location_count_less_10 else x)

df.drop(columns='Name', inplace=True)

X= df.drop(columns='Fees')
Y = df['Fees']

def onGetFee() :
    st.warning('This is a success message!')
    modal.predict(pd.DataFrame([{"Degree":degree, "Specialization":speciality, "Experience": experience, "Location": location, "City": city,"Recommendation": dp_score, "Feedback": npv }]))[0]

speciality = st.selectbox(
         label="Select Specialization", options=df["Specialization"].unique())

degree = st.selectbox(
       label="Select Degree", options=df["Degree"].unique())

experience = st.number_input("Years of Experience:", step=1)


location = st.selectbox(
       label="Select Location", options=df["Location"].unique())


city = st.selectbox(
         label="Select City", options=df["City"].unique())

dp_score = st.number_input("DP Score:", step=1)

npv = st.number_input("NPV:", step=1)

st.button(label="get Fee", on_click=onGetFee)