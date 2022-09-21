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

        if movie_dict["genre"] not in genre_freq_dict:
            genre_freq_dict[movie_dict["genre"]] = 1
        else:
            genre_freq_dict[movie_dict["genre"]] += 1
        print(f"genre_freq_dict: {genre_freq_dict}")
    
    if user_data["watched"] == []:
        max_genre = None
    else:
        max_genre = max(genre_freq_dict, key=genre_freq_dict.get)

    return max_genre
  

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


def get_unique_watched(user_data):
    #put each grouops watched movie titles in a set
    my_watched_set = set()
    friends_watched_set = set()

    for movie_dict in user_data["watched"]:
        my_watched_set.add(movie_dict["title"])
    
    for friends_list in user_data["friends"]:
        for friends_watched_dict, friends_watched_list in friends_list.items():
            for friends_movie_dict in friends_watched_list:
                friends_watched_set.add(friends_movie_dict["title"])

    
#compare sets and output movies in watched that aren't in friends
    user_watched_diffs_titles = my_watched_set.difference(friends_watched_set)
    user_watched_dif_list = []
    for movie_dict in user_data["watched"]:
        if movie_dict["title"] in user_watched_diffs_titles:
            user_watched_dif_list.append(movie_dict)
    return user_watched_dif_list

def get_friends_unique_watched(user_data):
    #put each grouops watched movie titles in a set
    my_watched_set = set()
    friends_watched_set = set()

    for movie_dict in user_data["watched"]:
        my_watched_set.add(movie_dict["title"])
    
    for friends_list in user_data["friends"]:
        for friends_watched_dict, friends_watched_list in friends_list.items():
            for friends_movie_dict in friends_watched_list:
                friends_watched_set.add(friends_movie_dict["title"])

    
#compare sets and output movies in friends that aren't in watched
    friends_watched_diffs_titles = friends_watched_set.difference(my_watched_set)
    friends_watched_dif_list = []

    for friends_list in user_data["friends"]:
        for friends_watched_dict, friends_watched_list in friends_list.items():
            for friends_movie_dict in friends_watched_list:
                if friends_movie_dict["title"] in friends_watched_diffs_titles:
                    friends_watched_dif_list.append(friends_movie_dict)

    return friends_watched_dif_list
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

