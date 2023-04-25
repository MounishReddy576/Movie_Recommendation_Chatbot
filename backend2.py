import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('./data/movies_metadata.csv', low_memory=False)

df = df[~df["title"].duplicated(keep='last')]
df = df[~df["title"].isna()]
df = df[~df["overview"].isna()]

tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(df['overview'])

cosine_sim = cosine_similarity(tfidf_matrix,
                               tfidf_matrix)

indices = pd.Series(df.index, index=df['title'])

def get_movie_recommends(name):

    try:
        movie_index = indices[name]
        cosine_sim[movie_index]

        similarity_scores = pd.DataFrame(cosine_sim[movie_index], columns=["score"])
        similarity_scores

        movie_indices = similarity_scores.sort_values("score", ascending=False)[1:11].index

        return df['title'].iloc[movie_indices]
    
    except:
        return []

# print(get_movie_recommends('Toy Story').to_list())
print(" * Backend2 stated: 'Movie Recommender [SIM2 Enabled]'")