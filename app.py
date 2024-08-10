import streamlit as st
import requests
from helper import *
import base64

st.set_page_config(
    page_title='Movie Recommendation System',
    page_icon='🎬',
    layout='wide'
)
st.header('Movie Recommendation System')

st.markdown(
    """
    <style>
    .cover-glow {
        width: 100%;
        height: auto;
        padding: 3px;
        box-shadow: 
            0 0 5px #275586,
            0 0 10px #275586,
            0 0 15px #275586,
            0 0 20px #275586,
            0 0 25px #275586,
            0 0 30px #275586,
            0 0 35px #275586;
        position: relative;
        z-index: -1;
        border-radius: 30px;  /* Rounded corners */
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def img_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

img_path = "imgs/logo1.jpg"
img_base64 = img_to_base64(img_path)
st.sidebar.markdown(
    f'<img src="data:image/png;base64,{img_base64}" class="cover-glow">',
    unsafe_allow_html=True,
)
st.sidebar.markdown("---")

def background():
    st.subheader('Most Popular Films of All Time')
    results = get_top50()
    images = list(results.values())
    captions = list(results.keys())    
    st.image(image=images,width=250,caption=captions)

with st.sidebar:
    option = st.selectbox(
        label='Recommendation based on',
        options=['Select an option','Movie','Genre','Director','Actor']
    )

if option=='Genre':
    with st.sidebar:
        genre = st.selectbox(
            label='Select your Genre',
            options=genre_list
        )
    if genre == 'Select an option':
        background()
    else:
        st.subheader(f'Top {genre} Movies of All Time')
        results = genrebased(genre)
        images = list(results.values())
        captions = list(results.keys())    
        st.image(image=images,width=250,caption=captions)

elif option=='Director':
    with st.sidebar:
        director = st.selectbox(
            label='Select your Director',
            options=director_list
        )
    if director == 'Select an option':
        background()
    else:
        st.subheader(f'Top Films Directed by {director}')
        results = directorbased(director)
        images = list(results.values())
        captions = list(results.keys())    
        st.image(image=images,width=250,caption=captions)

elif option=='Actor':
    with st.sidebar:
        actor = st.selectbox(
            label='Select your Actor',
            options=actors_list
        )
    if actor == 'Select an option':
        background()
    else:
        st.subheader(f'Top Films Featuring {actor}')
        results = actorbased(actor)
        images = list(results.values())
        captions = list(results.keys())   
        st.image(image=images,width=250,caption=captions)

elif option=='Movie':
    with st.sidebar:
        movie = st.selectbox(
            label='Select your Movie',
            options=movies_list
        )
    if movie == 'Select an option':
        background()
    else:
        st.subheader(f'Movies Similar to {movie}')
        results = moviebased(movie)
        images = list(results.values())
        captions = list(results.keys())    
        st.image(image=images,width=250,caption=captions)

else:
    background()
