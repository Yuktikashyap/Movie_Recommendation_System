import streamlit as st

st.title("Movie Recommendation System")

import pickle
import pandas as pd
import requests

movies = pickle.load(open('movies_dict.pkl' , 'rb'))
movies = pd.DataFrame(movies)

similar = pickle.load(open('similar.pkl','rb'))

selected_movie = st.selectbox("Search your movie here", movies['title'].values)

def get_poster(movie_id):

    r = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=c48f914994284ca388db45f2c916c78f&language=en-US".format(movie_id))
    data = r.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommend(movie):

      movie_ind = movies[movies['title'] == movie].index[0]
      movie_similar = similar[movie_ind]

      l = list(enumerate(movie_similar))

      movie_list = sorted(l,reverse = True,key = lambda x : x[1])[1:6] # give top 5 movies exclduign 0th = movie itself

      poster_list = []
      l2 = []

      for i in movie_list:
        l2.append(movies.iloc[i[0]].title)
        poster_list.append(get_poster(movies.iloc[i[0]].movie_id)) # instead of i[0] - > X movie id

      return l2,poster_list

if st.button('Recommended'):

    l1,l2 = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
       st.text(l1[0])
       st.image(l2[0])

    with col2:
       st.text(l1[1])
       st.image(l2[1])

    with col3:
       st.text(l1[2])
       st.image(l2[2])

    with col4:
       st.text(l1[3])
       st.image(l2[3])

    with col5:
       st.text(l1[4])
       st.image(l2[4])
