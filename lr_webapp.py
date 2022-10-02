# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle
import streamlit as st
from sklearn.utils._testing import assert_array_equal
from sklearn.utils._testing import assert_no_warnings
from sklearn.utils._testing import ignore_warnings


loaded_model=pickle.load(open('D:\cdrivefiles\Desktop\Random_Forest.sav','rb'))

def rf_prediction(input_data):

    input_num_arr=np.asarray(input_data)
    input_reshape=input_num_arr.reshape(1,-1)
    guess=loaded_model.predict(input_reshape)


    if(guess[0] == 0):
        return "no heart disease"
    elif(guess[0] == 1):
        return "heart disease"
    else:
        return "please enter correct details"
    
def main():
   # st.image("heart.jpg")
    st.title("Heart Disease Prediction using Random Forest")
    age=st.number_input("Enter the age")
    sex=st.number_input("Enter gender")
    cp=st.number_input("Enter cp")
    trestbps=st.number_input("Enter trestbps")
    chol=st.number_input("Enter chol")
    fbs=st.number_input("Enter fbs")
    restecg=st.number_input("Enter restecg")
    thalach=st.number_input("Enter thalach")
    exang=st.number_input("Enter exang")
    oldpeak=st.number_input("Enter oldpeak")
    slope=st.number_input("Enter slope")
    ca=st.number_input("Enter ca")
    thal=st.number_input("Enter thal")
    
    diagnosis=''
    
    
    if st.button("Heart disease result"):
        diagnosis = rf_prediction([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
        
    st.success(diagnosis)
    
if __name__ =='__main__':
    main()
