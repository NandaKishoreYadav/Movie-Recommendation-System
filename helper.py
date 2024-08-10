import pandas as pd
import ast
import requests

data = pd.read_csv('data/preprocessed_data.csv')
movie_posters = pd.read_csv('data/movie_posters.csv')

def get_poster(id):
    ind = movie_posters[movie_posters['movie_id'] == id].index[0]
    if not movie_posters.poster_link[ind]:
        return 'https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg?20200913095930'
    return movie_posters.poster_link[ind]

def directorbased(director):
    l={}
    for i in range(len(data)):
        if len(l)>=20:
            break
        if director in data.iloc[i].crew:
            l[data.iloc[i].title] = get_poster(data.iloc[i].id)
    return l

def actorbased(actor):
    l={}
    for i in range(len(data)):
        if len(l)>=20:
            break
        if actor in data.iloc[i].cast:
            l[data.iloc[i].title] = get_poster(data.iloc[i].id)
    return l

def genrebased(genre):
    l={}
    for i in range(len(data)):
        if len(l)>=20:
            break
        if genre in data.iloc[i].genres:
            l[data.iloc[i].title] = get_poster(data.iloc[i].id)
    return l

def moviebased(movie_name):
    movies = pd.read_csv('data/final_data.csv')
    from sklearn.feature_extraction.text import CountVectorizer
    cv=CountVectorizer(max_features=5000,stop_words='english')
    vector = cv.fit_transform(movies['tags']).toarray()
    from sklearn.metrics.pairwise import cosine_similarity
    similarity = cosine_similarity(vector)

    movie_id = movies[movies['title']==movie_name].index[0]
    mat = similarity[movie_id]
    l = {}
    mat = list(enumerate(mat))
    size = min(len(mat),12)
    mat = sorted(mat,reverse=True, key = lambda x:x[1])[1:size+1]
    
    for i in mat:
        l[data.iloc[i[0]].title] = get_poster(data.iloc[i[0]].id)
    print(l.keys())
    return l

def get_top50():
    df = pd.read_csv('data/tmdb_5000_movies.csv')
    sorted_df = df.sort_values(by='popularity', ascending=False)
    top_50_movies = sorted_df.head(50)

    l={}
    for i in range(50):
        l[top_50_movies.iloc[i].original_title] = get_poster(top_50_movies.iloc[i].id)
    return l


genre_list = set()
for genres in data['genres']:
    for genre in ast.literal_eval(genres):
        genre_list.add(genre)
genre_list = list(genre_list)
genre_list.sort()
genre_list = ['Select an option'] + genre_list

director_list = set()
for directors in data['crew']:
    for director in ast.literal_eval(directors):
        director_list.add(director)
director_list = list(director_list)
director_list.sort()
director_list = ['Select an option'] + director_list

actors_list = set()
for actors in data['cast']:
    for actor in ast.literal_eval(actors):
        actors_list.add(actor)
actors_list = list(actors_list)
actors_list.sort()
actors_list = ['Select an option'] + actors_list

movies_list = ['Select an option'] + list(data.title)

