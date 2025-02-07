import streamlit as st
import pickle
import numpy as np

# Load the Liver Disease model
with open("C:/Users/91701/Downloads/liver_disease_prediction.pkl", 'rb') as f:
    liver_model = pickle.load(f)

st.title("🍷 Liver Disease Prediction")

# Input fields for Liver Disease prediction
st.write("Please enter the following details:")
feature1 = st.number_input("Age")
feature2 = st.number_input("Gender")
feature3 = st.number_input("Total_Bilirubin")
feature4 = st.number_input("Direct_Bilirubinl")
feature5 = st.number_input("Alkaline_Phosphotase")
feature6 = st.number_input("Alamine_Aminotransferase")
feature7 = st.number_input("Aspartate_Aminotransferase")
feature8 = st.number_input("Total_Protiens")
feature9 = st.number_input("Albumin")
feature10 = st.number_input("Albumin_and_Globulin_Ratio")
# Add more features as needed

if st.button("Predict"):
    input_data = np.array([[feature1, feature2,feature3,feature4,feature5,feature6,feature7,feature8,
                            feature9,feature10]])  
    prediction = liver_model.predict(input_data)
    
    if prediction[0] == 1:
        st.error("The model predicts that the patient has Liver disease.")
    else:
        st.success("The model predicts that the patient does not have Liver disease.")