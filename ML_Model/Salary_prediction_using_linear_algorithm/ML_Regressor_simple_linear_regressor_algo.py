import numpy as np    
import pickle
import matplotlib.pyplot as plt
import pandas as pd    
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from statsmodels.api import OLS, add_constant

# Load the dataset
dataset = pd.read_csv(r"C:\Users\sagar\VS CODE\Regression\Salary_Data.csv")

# Split the data into independent (X) and dependent variables (y)
X = dataset.iloc[:, :-1].values  # Independent variable (Years of Experience)
y = dataset.iloc[:, 1].values    # Dependent variable (Salary)

# Split the dataset into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

# Initialize the Linear Regression model
regressor = LinearRegression()

# Train the model on the training data
regressor.fit(X_train, y_train)

# Predict the salaries for the test set
y_pred = regressor.predict(X_test)

# Visualize the Training Set results
plt.scatter(X_train, y_train, color='red')  # Scatter plot of actual data points
plt.plot(X_train, regressor.predict(X_train), color='blue')  # Regression line
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualize the Test Set results
plt.scatter(X_test, y_test, color='red')  # Scatter plot of actual data points
plt.plot(X_test, regressor.predict(X_test), color='blue')  # Regression line
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Predict the salary for 12 and 20 years of experience
y_12 = regressor.predict([[12]])  # Predict for 12 years of experience
y_20 = regressor.predict([[20]])  # Predict for 20 years of experience
print(f"Predicted salary for 12 years of experience: ${y_12[0]:,.2f}")
print(f"Predicted salary for 20 years of experience: ${y_20[0]:,.2f}")

# Check model performance using R^2 score and Mean Squared Error
bias = regressor.score(X_train, y_train)  # R^2 score for training data (bias)
variance = regressor.score(X_test, y_test)  # R^2 score for test data (variance)
train_mse = mean_squared_error(y_train, regressor.predict(X_train))  # MSE for training data
test_mse = mean_squared_error(y_test, y_pred)  # MSE for test data

# Print the performance metrics
print(f"Training Score (R^2): {bias:.2f}")
print(f"Testing Score (R^2): {variance:.2f}")
print(f"Training MSE: {train_mse:.2f}")
print(f"Test MSE: {test_mse:.2f}")

# Save the trained model to disk using pickle
filename = 'linear_regression_model.pkl'
with open(filename, 'wb') as file:
    pickle.dump(regressor, file)  # Save the model
print("Model has been pickled and saved as linear_regression_model.pkl")

# Calculate additional performance metrics: R^2, MSE, and RMSE
R2 = r2_score(y_test, y_pred)  # R^2 score
MSE = mean_squared_error(y_test, y_pred)  # Mean Squared Error
RMSE = np.sqrt(MSE)  # Root Mean Squared Error
print("R^2 Score:", R2)
print("MSE:", MSE)
print("RMSE:", RMSE)

# OLS (Ordinary Least Squares) model
# Prepare data for OLS
X_train_const = add_constant(X_train)  # Add constant term for OLS
ols_model = OLS(y_train, X_train_const).fit()  # Fit the OLS model
print(ols_model.summary())  # Print the OLS regression summary
