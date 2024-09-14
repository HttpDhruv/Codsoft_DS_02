IMDb Movies Analysis 

This project involves analyzing a dataset of IMDb movies in India to gain insights into movie ratings, votes, and trends over the years. The analysis includes data cleaning, handling missing values, and visualizing various aspects of movie data, such as rating distributions, relationships between votes and ratings, and rating trends over the years.

Features:
Data Loading: Loads the IMDb movies dataset from a CSV file with latin1 encoding.
Data Cleaning:
Drops rows with missing Rating or Votes.
Extracts and converts Year to an integer.
Extracts and converts Duration to numeric, filling missing values with the median.
Converts Votes to numeric, filling missing values with the median.
Drops any remaining rows with missing values in Year or Duration.
Visualization:
Distribution of Ratings: Shows the frequency distribution of movie ratings with a histogram.
Rating vs. Votes: Plots a scatter plot to visualize the relationship between the number of votes and movie ratings.
Average Rating by Year: Displays a line plot showing the average movie rating per year.

Prerequisites:
Python 3.x

Required Libraries:
pandas
numpy
matplotlib
seaborn
