import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dataset_path = '../dataset/IMDB-Movie-Data.csv'

# Read data with specified explicit index
data_indexed = pd.read_csv(dataset_path, index_col='Title')

# Read data from .csv file
data = pd.read_csv(dataset_path)

# 2,3. Understand the basic information about the data
# print(data.head(5))
# print(data.info())
# print(data.describe())

# 4. Data Selection Indexing and Slicing: Exatract data as series
genre = data['Genre']
# print(genre)

# 4. Data Selection Indexing and Slicing: Extract data as DataFrame
genre_col = data[['Genre']]
some_cols = data[["Title", "Genre", "Actors", "Director", "Rating"]]
some_rows = data.iloc[10:15][["Title", "Rating", "Revenue (Millions)"]]
# print(some_rows)

# 5. Data Selection Based on Conditional Filtering
data_filtered = data[((data['Year'] >= 2010) & (data['Year'] <= 2015))
                     & (data['Rating'] < 6.0)
                     & (data['Revenue (Millions)'] > data['Revenue (Millions)'].quantile(0.95))]
# print(data_filtered)

# 6. Groupby Operations
data_grouped = data.groupby('Director')[['Rating']].mean().head(5)
# print(data_grouped)

# 7. Sorting Operations
data_sorted = data.groupby('Director')[['Rating']].mean(
).sort_values(by='Rating', ascending=False).head(5)
# print(data_sorted)

# 8. View missing values
data_missing = data.isnull().sum()
# print(data_missing)

# 9. Dealing with missing values - Deleting: Use drop function to drop columns
data_dropped = data.drop("Metascore", axis=1).head()
data_row_dropped = data.dropna()
# print(data_dropped)
# print(data_row_dropped)

# 10. Dealing with missing values - Filling
revenue_mean = data_indexed['Revenue (Millions)'].mean()
# print("The mean revenue is: ", revenue_mean)

# Fill missing values with the mean revenue
data_filled = data_indexed['Revenue (Millions)'].fillna(
    revenue_mean, inplace=True)


# 11. apply() function: Classify movies based on their ratings
def rating_group(rating):
    if rating >= 7.5:
        return "Good"
    elif rating >= 6.0:
        return "Average"
    else:
        return "Bad"


# creating a new variables in the dataset to hold the rating category
data['Rating_category'] = data['Rating'].apply(rating_group)
data_rating_category = data[['Title', 'Director',
                             'Rating', 'Rating_category']].head(5)
print(data_rating_category)
