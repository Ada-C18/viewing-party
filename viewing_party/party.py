# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        new_movie = {
            "title": title,
            "genre": genre,
            "rating": rating
        }
        return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):

    for movie in user_data["watchlist"]:
        if title in movie["title"]:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            
    return user_data
            

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    total_ratings = 0
    number_of_movies = 0

    for movie_dict in user_data["watched"]:
        total_ratings += movie_dict["rating"]
        number_of_movies += 1

    if number_of_movies == 0:
        average_rating = 0.0
    else:
        average_rating = total_ratings/number_of_movies

    return average_rating

# my_data = {"watched": [{"title": "scary movie", "genre": "horror", "rating": "3"}, {"title": "another scary movie", "genre": "horror", "rating": "2"}, {"title": "funny movie", "genre": "comedy", "rating": "5"}]}
def get_most_watched_genre(user_data):
    genre_freq_dict = {}
    
    for movie_dict in user_data["watched"]:
        if user_data["watched"] == []:
            return None
        if movie_dict["genre"] not in genre_freq_dict:
            genre_freq_dict[movie_dict["genre"]] = 1
        else:
            genre_freq_dict[movie_dict["genre"]] += 1
        print(f"genre_freq_dict: {genre_freq_dict}")
    
    max_genre = max(genre_freq_dict, key=genre_freq_dict.get)

    return max_genre
  

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

