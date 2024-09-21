# Importing the required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

# Load the dataset
dataset = pd.read_csv(r"C:\Users\sagar\OneDrive\Desktop\Data science with GenAI\ML_implementions\Data.csv")

# Divide data into independent variables (X) and dependent variable (Y)
X = dataset.iloc[:, :-1].values  # All rows, all columns except the last
Y = dataset.iloc[:, 3].values  # Assuming the dependent variable is at index 3

# Handling missing values for columns 1 and 2 using SimpleImputer
imputer = SimpleImputer(strategy="mean")  # Default strategy is 'mean'
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

# Encoding categorical data in the independent variable (X)
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])  # Transform the first column

# Encoding the dependent variable (Y)
labelencoder_Y = LabelEncoder()
Y = labelencoder_Y.fit_transform(Y)

# Splitting the dataset into the training set and the test set
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Feature scaling using StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)  # Fit and transform the training set
X_test = sc_X.transform(X_test)  # Only transform the test set
