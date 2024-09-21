# Salary Prediction App using Simple Linear Regression 💼📈

I developed a **Salary Prediction App** using **Simple Linear Regression** to model the relationship between years of experience and salary. The project includes data preparation, model development, prediction, evaluation, and a front-end interface for users to interact with the model.

## 🔍 Data Preparation

- **Independent Variable**: Years of experience
- **Dependent Variable**: Salary
- The dataset was split into:
  - **80% Training Set**: To train the model
  - **20% Testing Set**: To validate the model

## 🛠️ Model Development

- **Algorithm**: Simple Linear Regression
- Trained the model using the training data (years of experience and salary).
- Saved the trained model using **pickle** for easy reuse.

## 🔮 Prediction

- Predicted salaries for the test data and compared them with actual salaries to evaluate the model's accuracy.
- Users can input specific years of experience and predict the corresponding salary using the model.

## 📊 Model Evaluation

- **Bias-Variance Trade-off**: Evaluated the model’s performance on training and test data.
- **Mean Squared Error (MSE)**: Measured the average squared difference between predicted and actual salaries.
- **R-squared (R²)**: Assessed how well the model explained the variability of the data.

## 🌐 Front-End Development

- Created an interactive front-end using **Streamlit**, where users can:
  - Enter the number of years of experience.
  - Predict the corresponding salary based on the trained model.

## 📚 Libraries Used

- **Pandas**: Data manipulation and analysis.
- **NumPy**: Numerical operations.
- **Scikit-learn**: Implementation of the Simple Linear Regression model.
- **Statsmodels**: Additional statistical modeling.
- **Pickle**: Model persistence (saving and loading the trained model).
- **Matplotlib**: Visualization of training and test results.
- **Streamlit**: Front-end development for the interactive app.

