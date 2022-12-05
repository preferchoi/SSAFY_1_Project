import requests
import json

TMDB_API_KEY = '94a2223b44d98108251e8243b8da5240'

def makejson():
    total_data = []
    for i in range(1, 51):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()

        for movie in movies['results']:
            if movie.get('release_date', ''):
                fields = {
                    'title': movie['title'],
                    'vote_average': movie['vote_average'],
                    'popularity': movie['popularity'],
                    'overview': movie['overview'],
                    'released_date': movie['release_date'],
                    'poster_path': movie['poster_path'],
                    'backdrop_path':movie['backdrop_path'],
                    'genres': movie['genre_ids'],
                }

                data = {
                    "pk": movie['id'],
                    "model": "movies.movie",
                    "fields": fields
                }

                total_data.append(data)

    with open("movies.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent="  ", ensure_ascii=False)

makejson()