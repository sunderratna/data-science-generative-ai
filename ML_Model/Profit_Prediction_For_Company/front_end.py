import streamlit as st
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

# Load the saved model
model = pickle.load(open(r'C:\Users\sagar\OneDrive\Desktop\Data science with GenAI\Projects\Profit_Prediction_For_Company\profit_pediction_model.pkl', 'rb'))

# Title of the app
st.title("Investment Profit Prediction App 💼")

# Brief description
st.write("""
    This app predicts the **Profit** based on investments in **Digital Marketing**, **Promotion**, **Research**, and **State**.
""")

# Sidebar for user input
st.sidebar.header("Input Investment Details")

# Define a function to take input features from the user
def user_input_features():
    digital_marketing = st.sidebar.number_input('Investment in Digital Marketing:', min_value=0.0, step=1000.0)
    promotion = st.sidebar.number_input('Investment in Promotion:', min_value=0.0, step=1000.0)
    research = st.sidebar.number_input('Investment in Research:', min_value=0.0, step=1000.0)
    state = st.sidebar.selectbox('State:', ('Hyderabad', 'Bangalore', 'Chennai'))
    
    # Create a dictionary for the inputs
    data = {'DigitalMarketing': digital_marketing,
            'Promotion': promotion,
            'Research': research,
            'State': state}
    
    features = pd.DataFrame(data, index=[0])
    return features

# Store the user input in a variable
input_df = user_input_features()

# One-hot encoding the 'State' column
input_df = pd.get_dummies(input_df, columns=['State'], drop_first=False)

# Ensure all dummy variables are present, even if not all states are selected
if 'State_Bangalore' not in input_df.columns:
    input_df['State_Bangalore'] = 0
if 'State_Chennai' not in input_df.columns:
    input_df['State_Chennai'] = 0
if 'State_Hyderabad' not in input_df.columns:
    input_df['State_Hyderabad'] = 0

# Reorder columns to match the model's expected input
input_df = input_df[['DigitalMarketing', 'Promotion', 'Research', 'State_Bangalore', 'State_Chennai', 'State_Hyderabad']]

# Show the input details
st.subheader('User Input details:')
st.write(input_df)

# Predict the profit using the input data
if st.button("Predict Profit"):
    prediction = model.predict(input_df)
    st.success(f"The predicted profit is: ${prediction[0]:,.2f}")

# Extra section for displaying information about the model
st.write("""
    This prediction is based on a Multiple Linear Regression (MLR) model that takes into account
    investments in Digital Marketing, Promotion, Research, and the State where the investment is made.
""")
