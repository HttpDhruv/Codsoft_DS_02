import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = r"C:\Users\dhrub\Downloads\codsoft ds dataset\IMDb Movies India.csv"
data = pd.read_csv(file_path, encoding='latin1')

# Handle missing values and convert data types
data = data.dropna(subset=['Rating', 'Votes'])  # Drop rows where 'Rating' or 'Votes' are NaN

# Convert 'Year' to integer
data['Year'] = data['Year'].str.extract('(\d+)')
data['Year'] = pd.to_numeric(data['Year'], errors='coerce')
data = data.dropna(subset=['Year'])
data['Year'] = data['Year'].astype(int)

# Extract numeric values from 'Duration' and convert to numeric
data['Duration'] = pd.to_numeric(data['Duration'].str.extract('(\d+)')[0], errors='coerce')

# Fill missing 'Duration' with the median value and convert to integer
data['Duration'] = data['Duration'].fillna(data['Duration'].median()).astype(int)

# Convert 'Votes' to numeric and fill NaN values with the median
data['Votes'] = pd.to_numeric(data['Votes'], errors='coerce')
data['Votes'] = data['Votes'].fillna(data['Votes'].median()).astype(int)

# Drop any remaining rows with missing values in 'Year' or 'Duration'
data = data.dropna(subset=['Year', 'Duration'])

# Distribution of Ratings
plt.figure(figsize=(10, 6))
sns.histplot(data['Rating'], bins=20, kde=True)
plt.title('Distribution of Movie Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()

# Rating vs. Votes
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Votes', y='Rating', data=data)
plt.title('Rating vs. Votes')
plt.xlabel('Votes')
plt.ylabel('Rating')
plt.show()

# Average Rating by Year
avg_rating_by_year = data.groupby('Year')['Rating'].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.lineplot(x='Year', y='Rating', data=avg_rating_by_year)
plt.title('Average Movie Rating by Year')
plt.xlabel('Year')
plt.ylabel('Average Rating')
plt.show()
