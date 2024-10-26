import streamlit as st
import pandas as pd
import pickle

# Load the pre-trained model
with open('model_regressor.pkl', 'rb') as file:
    model = pickle.load(file)
    

def age_to_category(age):
    if age > 18 and age < 25:
        return 1
    elif age > 24 and age < 30:
        return 2
    elif age > 29 and age < 35:
        return 3
    elif age > 34 and age < 40:
        return 4
    elif age > 39 and age < 45:
        return 5
    elif age > 44 and age < 50:
        return 6
    elif age > 49 and age < 55:
        return 7
    elif age > 54 and age < 60:
        return 8
    elif age > 59 and age < 65:
        return 9
    elif age > 64 and age < 70:
        return 10
    elif age > 69 and age < 75:
        return 11
    elif age > 74 and age < 80:
        return 12
    elif age > 80:
        return 13


age = st.number_input("Age", min_value=0, max_value=100, value=40)
gender = st.selectbox("Gender (0 : Female , 1: for Male)", [0, 1])
drinking = st.selectbox("Drinking Status (0 : Never Drinker , 1 : Ever Drinker)", [0 , 1])
smoking = st.selectbox("Smoking Status: (0: Never Smoker , 1: Ever Smoker)", [0 , 1])
BMI = st.number_input("BMI", min_value=0, max_value=100, value=25)
Chol = st.number_input("Cholesterol", min_value=0.0, max_value=20.0, value=4.5)
HDL = st.number_input("HDL (High-Density Lipoprotein)", min_value=0.0, max_value=7.0, value=1.5)
BUN = st.number_input("BUN (Blood urea nitrogen)", min_value=0.0, max_value=30.0, value=4.5)
Tri = st.number_input("Triglyceride", min_value=0.0, max_value=10.0, value=1.5)
CCR = st.number_input("CCR (Creatinine Clearance)", min_value=4.0, max_value=250.0, value=75.0)
LDL = st.number_input("LDL (Low-Density Lipoprotein)", min_value=0.0, max_value=7.0, value=2.82)
SBP = st.number_input("SBP (Systolic Blood Pressure)", min_value=0.0, max_value=200.0, value=120.0)
DBP = st.number_input("DBP (Diastolic Blood Pressure)", min_value=0.0, max_value=200.0, value=80.0)

convertedAge = age_to_category(age)

# Create a DataFrame from the inputs
input_data = pd.DataFrame({
    'Age': [age],
    'Gender': [gender],
    'drinking': [drinking],
    'smoking': [smoking],
    'BMI': [BMI],
    'Chol': [Chol],
    'HDL': [HDL],
    'BUN': [BUN],
    'Tri': [Tri],
    'CCR': [CCR],
    'LDL': [LDL],
    'SBP': [SBP],
    'DBP': [DBP]
})

input_data['Age'] = input_data['Age'].astype(int)

# Predict button
if st.button("Predict"):
    prediction = model.predict(input_data)
    predictedFPG = prediction[0][0] * 18.015
    predictedFFPG = prediction[0][1] * 18.015
    st.write(f"The Predicted Fasting Plasma Glucose is : {format(predictedFPG , '.2f')} mg/dl")
    st.write(f"The Predicted Final Fasting Plasma Glucose is : {format(predictedFFPG , '.2f')} mg/dl")