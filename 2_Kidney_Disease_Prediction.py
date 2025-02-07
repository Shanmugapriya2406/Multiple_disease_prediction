import streamlit as st
import pickle
import numpy as np
import sklearn

# Load the Kidney Disease model
with open('C:/Users/91701/Downloads/kidney_disease_prediction.pkl', 'rb') as f:
    kidney_model = pickle.load(f)

st.title("🩸 Kidney Disease Prediction")

# Input fields for Kidney Disease prediction
st.write("Please enter the following details:")
feature1 = st.number_input("age")
feature2 = st.number_input("bp")
feature3 = st.number_input("sg")
feature4 = st.number_input("al")
feature5 = st.number_input("su")
feature6 = st.number_input("rbc")
feature7 = st.number_input("pc")
feature8 = st.number_input("pcc")
feature9 = st.number_input("ba")
feature10 = st.number_input("bgr")
feature11 = st.number_input("bu")
feature12 = st.number_input("sc")
feature13 = st.number_input("pot")
feature14 = st.number_input("wc")
feature15 = st.number_input("rc")
feature16 = st.number_input("htn")
feature17 = st.number_input("dm")
feature18 = st.number_input("cad")
feature19 = st.number_input("appet")
feature20 = st.number_input("pe")
feature21 = st.number_input("ane")
# Add more features as needed

if st.button("Predict"):
    input_data = np.array([[feature1, feature2,feature3,feature4,feature5,feature6,feature7,feature8,feature9,feature10,feature11,
                            feature12,feature13,feature14,feature15,feature16,feature17,feature18,feature19,feature20,feature21]])
    prediction = kidney_model.predict(input_data)
    
    if prediction[0] == 1:
        st.error("The model predicts that the patient has Kidney disease.")
    else:
        st.success("The model predicts that the patient does not have Kidney disease.")
