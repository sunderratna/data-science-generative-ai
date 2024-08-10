# IPL Player Data Analysis

## Overview

This work provides an in-depth analysis of IPL player data, focusing on salaries, games played, and points scored across ten seasons (2015-2024). The analysis aims to uncover trends, patterns, and insights into player performance and earnings over the years.

## Project Objectives

- **Visualize player salaries over multiple seasons** to identify trends and fluctuations.
- **Analyze the number of games played by each player** to understand their participation and consistency.
- **Evaluate points scored by players** to assess performance and impact on their teams.
- **Compare players** across these metrics to gain insights into their career progression and value to their teams.

## Steps Followed

### 1. Library Imports
- **`numpy`**: Used for efficient numerical operations and data management.
- **`matplotlib`**: Employed for plotting and visualizing the trends in the data.
- **`warnings`**: Utilized to suppress irrelevant warnings to ensure clean output.

### 2. Data Initialization
- **Seasons and Players**: Lists and dictionaries were created to represent seasons from 2015 to 2024 and a selection of IPL players, respectively.
- **Salary, Games, and Points Data**: Data arrays were initialized for each player, capturing their salary, games played, and points scored in each season.

### 3. Data Transformation
- **Conversion to `numpy` Arrays**: The raw lists of data were converted into `numpy` arrays, which facilitate easier manipulation, calculation, and plotting.
- **Matrix Representation**: Salaries, games played, and points scored were organized into matrices where rows represent players, and columns represent seasons.

### 4. Data Visualization
- **Plotting Salaries**: Salary trends for each player across the seasons were plotted to identify growth, stability, or decline.
- **Games Played Analysis**: A plot of the number of games played by each player each season provided insights into their participation and fitness levels.
- **Performance (Points Scored)**: Points scored by each player were plotted to evaluate their contribution and effectiveness on the field.

## Data Details

- **Seasons (2015-2024)**: Represents each year of the analysis period.
- **Players**: Includes ten notable IPL players such as Sachin, Rahul, and Kohli.
- **Salaries**: Annual earnings of each player, indicating their market value and contract terms over the years.
- **Games Played**: The number of matches each player participated in during each season, reflecting their engagement and selection by teams.
- **Points Scored**: A measure of each player's on-field performance, likely reflecting runs scored in the context of cricket.

## Plotting Results

Three key plots were generated to visualize the data:

1. **Salary Trends Plot**:
   - Showcases the annual salaries of each player over ten seasons.
   - Helps in understanding contract changes, player demand, and financial growth.

2. **Games Played Plot**:
   - Illustrates the number of games each player participated in each season.
   - Provides insights into player availability, fitness, and team reliance.

3. **Points Scored Plot**:
   - Visualizes the performance of each player in terms of points scored.
   - Helps in identifying consistent performers and those with fluctuating performance levels.

## Example Plots

- **Salary Trends**: Identifies top earners and those with significant salary changes.
- **Games Played**: Highlights players with high participation versus those with gaps.
- **Points Scored**: Points to the players who have consistently contributed to their teams.

## Installation

To run this analysis, you need Python installed along with the following libraries:

```bash
pip install numpy matplotlib
