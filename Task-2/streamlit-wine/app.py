import streamlit as st
# from PIL import Image
# import requests
# import hopsworks
import joblib
import pandas as pd
import numpy as np
# project = hopsworks.login()
# fs = project.get_feature_store()


# mr = project.get_model_registry()
# model = mr.get_model("wine_model", version=1)
model = joblib.load("Task-2/wine_model/wine_model.pkl")
print("Model Loaded")

st.title('Wine Quality Predictor - ID2223')

col1, col2 = st.columns(2)
with col1:
    type = st.number_input("type")
    fixed_acidity = st.number_input('fixed_acidity')
    volatile_acidity = st.number_input('volatile_acidity')
    citric_acid = st.number_input('citric_acid')
    residual_sugar = st.number_input('residual_sugar')
    chlorides = st.number_input('chlorides')
    free_sulfur_dioxide = st.number_input('free_sulfur_dioxide')
    total_sulfur_dioxide = st.number_input('total_sulfur_dioxide')
    density = st.number_input('density')
    ph = st.number_input('ph')
    sulphates = st.number_input('sulphates')
    alcohol = st.number_input('alcohol')

    data = pd.DataFrame([type, fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, ph, sulphates, alcohol]).T
    print(data)

with col2:
    if st.button('Predict Wine Quality'):
        y_pred = model.predict(data)
        wine = y_pred[0]
        st.write("Wine Quality Predicted: " + str(wine))
    else:
        st.write("Press Button to Begin")

    