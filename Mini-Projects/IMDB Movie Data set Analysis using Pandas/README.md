![Python](https://img.shields.io/badge/Python-3.x-blue.svg?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-1.x-%23150458.svg?logo=pandas)


# IMDB Movie Data set Analysis using Pandas
## Overview

This project provides a comprehensive analysis of IMDB movie data. Using a dataset of movies, tags, and ratings, we perform data exploration, cleaning, and visualization to uncover insights about movie ratings, genres, and user interactions.
## 📥 Libraries Used

    Pandas: For data manipulation and analysis.
    Matplotlib: For data visualization.
    Warnings: To handle warnings during analysis.

## 📅 Datasets

    Movies Dataset: Contains movie details including title, genres, and movie IDs.
    Tags Dataset: Includes user-generated tags associated with movies.
    Ratings Dataset: Provides ratings given by users to movies.

## 🔧 Data Cleaning

    Column Removal: The 'timestamp' column was removed from both the tags and ratings datasets as it was not required for analysis.
    Handling Missing Values: Rows with missing values in the tags dataset were dropped to ensure data integrity.

## 📊 Data Exploration
### Series and DataFrames

    Explored Series objects for integer-based indexing.
    Examined DataFrames for structure and content, including indices and columns.

## Descriptive Statistics

    Calculated various statistics for the ratings dataset, including mean, median, standard deviation, and more.

## Data Visualization

    Histograms: Visualized the distribution of movie ratings.
    Boxplots: Examined the spread and outliers in the ratings dataset.
    Bar Charts: Displayed the most frequent movie tags and genres.

## 🎣 Filters and Aggregation

    Filters: Applied filters to select highly-rated movies and those with specific genres.
    Aggregation: Grouped data to calculate average ratings and count ratings per movie.

## 🔰 Merging DataFrames

    Merged the movies and tags datasets to create a comprehensive view of movie information and associated tags.
    Combined average ratings with movie details to analyze ratings across different genres.

## 📚 Advanced Analysis

    Vectorized String Operations: Split genres into multiple columns and created flags for specific genres such as Comedy.
    Year Extraction: Extracted the release year from movie titles for additional analysis.

## Conclusion

This analysis provides valuable insights into movie ratings and genres, helping to understand user preferences and movie popularity. The findings include trends in rating distributions, genre popularity, and the impact of specific tags on movie ratings.
