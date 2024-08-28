![Python](https://img.shields.io/badge/Python-3.x-blue.svg?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-1.x-%23150458.svg?logo=pandas)
![Seaborn](https://img.shields.io/badge/Seaborn-0.11.0-%23007A87.svg?logo=seaborn)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-%23ff69b4.svg?logo=plotly)

# Movie Ratings Analysis and Visualization

This project involves analyzing a dataset of movie ratings using Pandas and advanced visualization techniques with Seaborn. The main goal is to uncover which genre of movies has the highest success rate, along with patterns and insights related to critic and audience ratings, and genre-wise budgets.

## Project Overview

- **Dataset**: The dataset includes movies, their genres, critic ratings, audience ratings, budgets, and release years.
- **Libraries Used**: Pandas, Seaborn, Matplotlib.

## Key Steps

1. **Loading the Dataset**:
   - The dataset is loaded using Pandas and basic information such as shape, columns, and data types are explored.

2. **Data Cleaning and Transformation**:
   - Columns are renamed for clarity.
   - Appropriate data types are set for categorical variables like `Film`, `Genre`, and `Year`.

3. **Descriptive Statistics**:
   - Basic descriptive statistics are generated to understand the distribution of numerical features.

4. **Visualization**:
   - Various plots are created to explore the relationship between critic and audience ratings, and the distribution of budgets across genres.
   - Joint plots, distribution plots, histograms, KDE plots, box plots, and violin plots are used for comprehensive analysis.

5. **Insights**:
   - Audience ratings tend to be more dominant compared to critic ratings.
   - Certain genres, like Drama, tend to have higher budgets and ratings.

## Conclusion

This analysis provides valuable insights into how movies are rated by critics and audiences, and how these ratings vary across different genres and budgets. The visualizations help in identifying patterns that could be useful for further decision-making or research.

