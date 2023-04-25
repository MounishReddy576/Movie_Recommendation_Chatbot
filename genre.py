import pandas as pd
import random

df = pd.read_csv('./data/genre.csv')

def get_genre_recommendations(genre):

    # Filter the DataFrame based on the genre
    filtered_df = df[df['Genre'].str.lower() == genre.lower()]

    # Randomly pick 3 movies from the filtered DataFrame
    selected_movies = filtered_df.sample(n=3, replace=False, random_state=None)["Name"]

    return selected_movies

# print(get_genre_recommendations('action').to_list())
print(" * Backend started: 'Genre Recommender'")