import streamlit as st
import pickle
import numpy as np
import xgboost

with open("C:/Users/91701/Downloads/parkinson_prediction.pkl", 'rb') as f:
    parkinson_model = pickle.load(f)

st.title("🧠 Parkinson's Disease Prediction")

st.write("Please enter the following details:")
feature1 = st.number_input("MDVP:Fo(Hz)")
feature2 = st.number_input("MDVP:Fhi(Hz)")
feature3 = st.number_input("MDVP:Flo(Hz)")
feature4 = st.number_input("MDVP:Jitter(%)")
feature5 = st.number_input("MDVP:Jitter(Abs)")
feature6 = st.number_input("MDVP:RAP")
feature7 = st.number_input("MDVP:PPQ")
feature8 = st.number_input("Jitter:DDP")
feature9 = st.number_input("MDVP:Shimmer")
feature10 = st.number_input("MDVP:Shimmer(dB)")
feature11 = st.number_input("Shimmer:APQ3")
feature12 = st.number_input("Shimmer:APQ5")
feature13 = st.number_input("MDVP:APQ")
feature14 = st.number_input("Shimmer:DDA")
feature15 = st.number_input("NHR")
feature16 = st.number_input("HNR")
feature17 = st.number_input("RPDE")
feature18 = st.number_input("DFA")
feature19 = st.number_input("spread1")
feature20 = st.number_input("spread2")
feature21 = st.number_input("D2")
feature22 = st.number_input("PPE")

if st.button("Predict"):
    input_data = np.array([[feature1, feature2,feature3,feature4,feature5,feature6,feature7,feature8,feature9,feature10,feature11,feature12,feature13,feature14,feature15,feature16,
                            feature17,feature18,feature19,feature20,
                            feature21,feature22]])  
    prediction = parkinson_model.predict(input_data)
    
    if prediction[0] == 1:
        st.error("The model predicts that the patient has Parkinson's disease.")
    else:
        st.success("The model predicts that the patient does not have Parkinson's disease.")
