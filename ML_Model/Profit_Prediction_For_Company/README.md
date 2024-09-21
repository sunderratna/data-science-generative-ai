# Investment Profit Prediction App

## Overview

This project involves building an **Investment Profit Prediction App** using a Multiple Linear Regression (MLR) model. The app predicts potential profit based on investments in Digital Marketing, Promotion, Research, and the State of operation.

## How It Works

### Data Preparation

1. **Dataset**: The project uses a CSV file named `Investment.csv` which includes data on investments and profit.
2. **Preprocessing**:
    - **Encoding**: Categorical data (State) is converted into numerical format using one-hot encoding.
    - **Splitting**: The dataset is divided into training and testing sets.

### Model Building

1. **Training**:
    - A Multiple Linear Regression (MLR) model is created and trained using scikit-learn.
    - The model is evaluated for performance using metrics such as R^2 Score, Mean Squared Error (MSE), and Root Mean Squared Error (RMSE).

2. **Statistical Analysis**:
    - An Ordinary Least Squares (OLS) model summary is generated to provide detailed statistical insights into the model.

### Application

1. **Streamlit App**:
    - **User Interface**: Users can input values for investments in Digital Marketing, Promotion, Research, and select a State.
    - **Prediction**: The trained model predicts profit based on the input values and displays the result.

2. **Model Deployment**:
    - The trained model is serialized using `pickle` and loaded by the Streamlit app to provide real-time predictions.

## Project Files

- **`Investment.csv`**: Dataset used for training the model.
- **`investment_profit_prediction.py`**: Script for training and saving the MLR model.
- **`front_end.py`**: Streamlit script for the interactive web application.
- **`profit_prediction_model.pkl`**: Pickled MLR model.

## Model Evaluation

The model's performance is assessed using the following metrics:
- **R^2 Score**: Measures how well the model explains the variability of the response data.
- **Mean Squared Error (MSE)**: Indicates the average squared difference between observed and predicted values.
- **Root Mean Squared Error (RMSE)**: Provides the square root of MSE, representing the standard deviation of residuals.
