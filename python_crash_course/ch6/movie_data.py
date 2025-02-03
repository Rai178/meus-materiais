movie_database = {}

movie_database['tt0111161'] = {'title': 'The Shawshank Redemption', 'director': 'Frank Darabont', 'genre': 'Drama', 'release_year': 1994}
movie_database['tt0468569'] = {'title': 'The Dark Knight', 'director': 'Christopher Nolan', 'genre': 'Action', 'release_year': 2008}
movie_database['tt0137523'] = {'title': 'Fight Club', 'director': 'David Fincher', 'genre': 'Drama', 'release_year': 1999}

def search_movie(movie_id):
    if movie_id in movie_database:
        print("Movie Information:")
        movie_info = movie_database[movie_id]
        for key, value in movie_info.items():
            print(f"{key}:{value}")
    else:
        print("movie not found in the database")