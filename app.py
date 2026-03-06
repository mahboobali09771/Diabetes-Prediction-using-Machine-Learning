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

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Diabetes Detected")
    else:
        st.success("No Diabetes")