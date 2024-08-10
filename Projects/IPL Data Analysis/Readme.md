# IPL Player Data Analysis

## Overview

This project analyzes IPL player data, including their salaries, games played, and points scored across multiple seasons. The aim is to visualize trends and compare player performance and earnings over the years.

## Steps

1. **Import Libraries**:
   - Import essential libraries such as `numpy` for numerical operations and `matplotlib` for plotting visualizations.

2. **Initialize Data**:
   - Define lists for seasons and players, and create dictionaries to map these to indices.
   - Initialize data arrays for player salaries, games played, and points scored for each season.

3. **Create Data Matrices**:
   - Convert the raw data into `numpy` arrays for easier manipulation and plotting.

4. **Calculate and Display Data**:
   - Calculate additional metrics as needed (e.g., salary per game) and display the raw data.

5. **Plotting**:
   - Generate plots to visualize salary trends, games played, and points scored over the seasons.

## Necessary Libraries

- **`numpy`**: Used for handling numerical operations and managing data arrays.
- **`matplotlib`**: Utilized for creating plots and visualizing data trends.
- **`warnings`**: Used to suppress warnings related to library updates.

## Data

- **Seasons**: The years ranging from 2015 to 2024.
- **Players**: A list of cricket players analyzed in the dataset.
- **Salaries**: Annual salaries for each player across the seasons.
- **Games Played**: Number of games played by each player during each season.
- **Points**: Points scored by each player across the seasons.

## Plotting

The project includes visualizations for:

1. **Salary Trends**: Plotting player salaries over the seasons to observe changes and trends.
2. **Games Played**: Tracking the number of games played by each player to analyze their participation over time.
3. **Points Scored**: Visualizing the points scored by players to assess their performance over the seasons.

### Example Plots

- **Salary Trends Plot**: Shows how the salary of each player changes over different seasons.
- **Games Played Plot**: Displays the number of games played by each player across seasons.
- **Points Scored Plot**: Illustrates the points scored by each player over the years.

## Installation

To run this project, you need to have Python and the following libraries installed:

```bash
pip install numpy matplotlib
