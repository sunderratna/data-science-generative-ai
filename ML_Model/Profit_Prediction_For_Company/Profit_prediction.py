import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the dataset
dataset = pd.read_csv(r"C:\Users\sagar\OneDrive\Desktop\Data science with GenAI\12th 11th sep- mlr\11th- mlr\MLR\Investment.csv")

# Split the dataset into independent (X) and dependent (y) attributes
X = dataset.iloc[:, :-1]  # Independent variables (all columns except the last one)
y = dataset.iloc[:, 4]    # Dependent variable (the last column, index 4)

# Convert categorical data into numerical format using one-hot encoding
X = pd.get_dummies(X, dtype=int)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create and train the Linear Regression model
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predict the target variable using the test set
y_pred = regressor.predict(X_test)

# Evaluate the model's performance
# Calculate the R^2 score, MSE, and RMSE for the test set predictions
R2 = r2_score(y_test, y_pred)
MSE = mean_squared_error(y_test, y_pred)
RMSE = np.sqrt(MSE)

print("R^2 Score:", R2)
print("MSE:", MSE)
print("RMSE:", RMSE)

# Add the intercept term to the features for OLS regression
c = regressor.intercept_
X = np.append(arr=np.full((50, 1), c).astype(int), values=X, axis=1)

# Perform Ordinary Least Squares (OLS) regression
regressor_OLS = sm.OLS(y, X).fit()
print(regressor_OLS.summary())  # Display the OLS regression summary

# Save the trained model using pickle
filename = "profit_prediction_model.pkl"
with open(filename, "wb") as file:
    pickle.dump(regressor, file)
print("Model has been pickled and saved as profit_prediction_model.pkl")
