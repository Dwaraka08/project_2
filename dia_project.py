import streamlit as st
import tensorflow as tf
import numpy as np

#load the model
diabates_model=tf.keras.models.load_model("F:/dia_prediction.h5")

#Title of the project 
st.title("Diabates Predition")
col1,col2=st.columns(2)

with col1:
    pregnanacies=st.text_input("Enter the Pregenancies")
    Glucose=st.text_input("Enter the Glucose level")
    Bp=st.text_input("Enter you Blood Pressures")
    skin_th=st.text_input("Enter the Skin Thickness")
    Insulin=st.text_input("Enter the Insulin level")
    bmi=st.text_input("Enter the BMI level")
    dpf=st.text_input("Enter the DiabatesPedigreeFunction")
    age=st.text_input("Enter your age")

with col2:
    st.image(r"F:\Heart_1.png")
if st.button("prediction"):
    data=[[pregnanacies,Glucose,Bp,skin_th,Insulin,bmi,dpf,age]]
    #data_filtered = [x for x in data if x != '']
    data_arry = np.array(data, dtype=float).reshape(1,-1)
    prediction=diabates_model.predict(data_arry)
    if prediction==1:
        st.write("Diabatic")
    else:
        st.write("non-Diabatic")