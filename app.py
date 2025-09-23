from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
import pickle
import pandas as pd
import requests
import os
import gdown

app = FastAPI()

# ---------- CORS (allow frontend requests) ----------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- Serve frontend ----------
@app.get("/")
def serve_index():
    return FileResponse("index.html")   # index.html must be in same folder as app.py


# ---------- Load data ----------

# Ensure movies_dictionary.pkl exists
if not os.path.exists("movies_dictionary.pkl"):
    # change this URL to a "uc?export=download" format so gdown works
    url = "https://drive.google.com/uc?id=1ELqd7chpU4LxhiLd1KEyeFHIKuEF5Ms1"
    # use fuzzy=True to allow using the original link or similar link
    gdown.download(url, "movies_dictionary.pkl", quiet=False, fuzzy=True)

# load movies list
movies_list = pickle.load(open("movies_dictionary.pkl", "rb"))



# Ensure cosine_similarity.pkl exists
if not os.path.exists("cosine_similarity.pkl"):
    url = "https://drive.google.com/uc?id=1TzR82vf9JDxSZR04sX7lDdowTINbqoY0"
    gdown.download(url, "cosine_similarity.pkl", quiet=False)

with open("cosine_similarity.pkl", "rb") as f:
    similarity = pickle.load(f)


# ---------- Utility functions ----------
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get("poster_path")
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path if poster_path else ""
    return full_path


def recommend(movie):
    movie_index = movies_list[movies_list["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list_1 = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list_1:
        movie_id = movies_list.iloc[i[0]].movie_id
        recommended_movies.append(movies_list.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters


# ---------- API Endpoints ----------
@app.get("/movies")
async def get_movies():
    """Return list of all movies (for dropdown/search)"""
    return {"movies": movies_list["title"].tolist()}


@app.get("/recommend")
async def get_recommendations(movie: str):
    try:
        names, posters = recommend(movie)

        if "genres" in movies_list.columns:
            genre = movies_list[movies_list["title"] == movie]["genres"].values[0]
        else:
            genre = "Unknown"

        return JSONResponse(
            content={
                "movie": movie,
                "genre": genre,
                "names": names,
                "posters": posters,
            }
        )
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)
