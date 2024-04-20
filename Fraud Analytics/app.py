import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import streamlit as st
import joblib

# Define the provided dataset
data = pd.read_csv('clean_data.csv')

# Assuming 'Is Fraudulent' is the target column, split data into features (X) and target (y)
X = data.drop(columns="Is Fraudulent", axis=1)
y = data["Is Fraudulent"]

# Load pre-trained best model
model = joblib.load('trans_fraud.pkl')

# Create Streamlit app
st.title("Transactional Fraud Detection Model")
st.write("Enter the following features to check if the transaction is legitimate or fraudulent:")

# Create input fields for the user to enter feature values
input_amount = st.text_input('Transaction Amount')
input_quantity = st.text_input('Quantity')
input_customer_age = st.text_input('Customer Age')
input_account_age = st.text_input('Account Age (Days)')
input_transaction_hour = st.text_input('Transaction Hour')
input_payment_method = st.text_input('Payment Method (encoded)')
input_product_category = st.text_input('Product Category (encoded)')
input_device_used = st.text_input('Device Used (encoded)')

# Create a button to submit input and get prediction
submit = st.button("Submit")

if submit:
    try:
        # Get input feature values and convert them to floats
        features = np.array([
            float(input_amount),
            float(input_quantity),
            float(input_customer_age),
            float(input_account_age),
            float(input_transaction_hour),
            float(input_payment_method),
            float(input_product_category),
            float(input_device_used)
        ])
        # Make prediction
        prediction = model.predict(features.reshape(1, -1))
        # Display result
        if prediction[0] == 0:
            st.write("Legitimate Transaction")
        else:
            st.write("This account Fraudulent Transaction Indicated")
    except ValueError:
        st.write("Error: Please enter the correct values for all features.")
