import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("model.pkl","rb"))

st.title("Diabetes Prediction App")

preg = st.number_input("Pregnancies")
glucose = st.number_input("Glucose")
bp = st.number_input("Blood Pressure")
skin = st.number_input("Skin Thickness")
insulin = st.number_input("Insulin")
bmi = st.number_input("BMI")
dpf = st.number_input("Diabetes Pedigree Function")
age = st.number_input("Age")

if st.button("Predict"):

    input_data = np.array([[preg,glucose,bp,skin,insulin,bmi,dpf,age]])

 prob = model.predict_proba(input_data)[0][1]

if prob < 0.3:
    st.success(f"Low future diabetes risk ({prob*100:.2f}%)")

elif prob < 0.7:
    st.warning(f"Moderate future diabetes risk ({prob*100:.2f}%)")

else:
    st.error(f"High future diabetes risk ({prob*100:.2f}%)")
