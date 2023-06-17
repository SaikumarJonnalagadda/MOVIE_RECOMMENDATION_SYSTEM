import streamlit as st
import pandas as pd
import numpy as np
import pickle

simi = pickle.load(open('simi.pkl','rb'))
final_df = pickle.load(open('final_df.pkl','rb'))
movies = pd.DataFrame(final_df)
st.title('Recommender')

select_movie = st.selectbox(
    'How would you like to be contacted?',
    (movies['title'].values))

st.write('You selected:', select_movie)


def movie_recommend(movie):
    movie_index = movies[movies['title']== movie].index[0]
    distances = simi[movie_index]
    movies_lst = sorted(list(enumerate(distances)),reverse=True,key=lambda x : x[1])[1:6]

    recommended_movies = []
    for i in movies_lst:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


if st.button('Recommend'):
    recommendations = movie_recommend(select_movie)
    for i in recommendations:
        st.write(i)