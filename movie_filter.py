import pandas as pd
from mood_handler import GetGenreFromMood
from file_loader import loadMovies

def getMoviesByGenre(genres, movies, top_n=5):

    if movies is None or genres is None:
        print("No movies and genre data found!")
        return pd.DataFrame()
    
    #Fill empty values with an empty string
    movies['genre'] = movies['genre'].fillna('')

    #Convert all genres to lowercase for easy comparison
    genres = [g.lower() for g in genres]
    
    #Check if genre is in movie genres
    def matches(movieGenres):
        movieGenres = [g.strip().lower() for g in movieGenres.split(',')]
        matches = any(g in movieGenres for g in genres)
        return matches
    
    #Filter the movies based on the genre value and store in a new dataframe
    user_movies = movies[movies['genre'].apply(matches)]

    #Return the top N values
    return user_movies.head(top_n)


def getMoviesByKeyword(keyword, movies, top_n=5):

    if movies is None or keyword is None:
        print("No movies or keyword data found!")
        return pd.DataFrame()
    
    matches = movies[
        movies['title'].str.lower().str.contains(keyword, na=False) |
        movies['director'].str.lower().str.contains(keyword, na=False)
    ]

    return matches.head(top_n)

def getMoviesByReleaseYear(year, movies, top_n=5):
    if movies is None or year is None:
        print("No movies or valid year found!")
        return pd.DataFrame()
    
    matches = movies[movies['release_year'] == year]

    return matches.head(top_n)

def getRandomMovies(count, movies):
    if movies is None or count is None:
        print("No movies or count data found!")
        return pd.DataFrame()
    
    top_movies = movies.sort_values(by='rating', ascending = False).head(200)
    return top_movies.sample(n = min(count, len(top_movies))).reset_index(drop=True)
    
