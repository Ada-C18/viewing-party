
# ------------- WAVE 1 --------------------


def create_movie(title, genre, rating):
    new_movie = {}
    if not title or not genre or not rating:
        return None
    new_movie["title"] = title
    new_movie["genre"] = genre
    new_movie["rating"] = rating
    
    return new_movie


def add_to_watched(user_data, movie):
    user_data["watched"] = []
    user_data["watched"].append(movie)

    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"] = []
    user_data["watchlist"].append(movie)

    return user_data


def watch_movie(user_data, title):
    for value in range(len(user_data["watchlist"])):
        
        if user_data["watchlist"][value]["title"] == title:
            move_to_watched = user_data["watchlist"][value]
            
            user_data["watched"].append(move_to_watched)
            user_data["watchlist"].pop(0)

    return user_data



# ------------- WAVE 2 --------------------



def get_watched_avg_rating(user_data):
    rating_sum = 0.0
    for value in range(len(user_data["watched"])):
        rating_sum += user_data["watched"][value]["rating"]
        average = rating_sum / len(user_data["watched"])
    
    if user_data["watched"] == []:
        average = 0.0

    return average


def get_most_watched_genre(user_data):
    genre_counts = {}
    
    if user_data["watched"] == []:
        return None

    for value in user_data["watched"]:
        if not value["genre"] in genre_counts.keys():
            genre_counts[value["genre"]] = 1
        elif value["genre"] in genre_counts.keys():
            genre_counts[value["genre"]] += 1

    for key,value in genre_counts.items():
        if value == max(genre_counts.values()):
            popular_genre = key

    return popular_genre



# ------------- WAVE 3 --------------------



def get_friends_movies(user_data):
    unique_watched = []
    friends_watched_list_of_dicts = user_data["friends"]

    for index in range(len(friends_watched_list_of_dicts)):
        for index_2 in range(len(friends_watched_list_of_dicts[index]["watched"])):
            unique_watched.append(friends_watched_list_of_dicts[index]["watched"][index_2])

    return unique_watched


def get_unique_watched(user_data):
    unique_movies = []
    user_watched_list = user_data["watched"]
    friends_watched_list = get_friends_movies(user_data)

    for index in range(len(user_watched_list)):
        if not user_watched_list[index] in friends_watched_list:
            unique_movies.append(user_watched_list[index])
    
    return unique_movies


def get_friends_unique_watched(user_data):
    not_watched_by_user = []
    friends_watched_list = get_friends_movies(user_data)
    user_watched_list = user_data["watched"]

    for movie in friends_watched_list:
        if not movie in user_watched_list and not movie in not_watched_by_user:
            not_watched_by_user.append(movie)
    
    return not_watched_by_user



# ------------- WAVE 4 --------------------



def get_available_recs(user_data):
    recommended_movies = []
    user_watched_list = user_watched_movies(user_data)
    friend_movies_data = compiled_friends_watched(user_data)
    user_subscriptions = user_data["subscriptions"]

    for friend_movie in friend_movies_data:
        title = friend_movie["title"]
        host = friend_movie["host"]

        if title not in user_watched_list and host in user_subscriptions:
            recommended_movies.append(friend_movie)

    return recommended_movies


#Returns a list with compiled dictionaries of ALL friends watched movies and its corresponding data.
def compiled_friends_watched(user_data):
    friends = user_data["friends"]
    all_movie_data_friends = []
    
    for index in range(len(friends)):
        individual_dicts = friends[index]
        list_of_dicts_within_dict = individual_dicts['watched']
        
        for item in list_of_dicts_within_dict:
            if item not in all_movie_data_friends:
                all_movie_data_friends.append(item)

    return all_movie_data_friends


#Returns a list of all movie titles watched by user
def user_watched_movies(user_data):
    watched_list_of_dicts = user_data["watched"]

    titles_list = []
    for movie_dict in watched_list_of_dicts:
        titles_list.append(movie_dict["title"])

    return titles_list



# ------------- WAVE 5 --------------------



import statistics

def get_new_rec_by_genre(user_data):
    user_genre = user_most_watched_genre(user_data)
    user_watched_titles_list = user_watched_movies(user_data)
    friends_watched_data_list = compiled_friends_watched(user_data)

    movie_recs = []

    for movie in friends_watched_data_list:
        if movie["genre"] == user_genre and movie["title"] not in user_watched_titles_list:
            movie_recs.append(movie)

    return movie_recs


# Helper Function: returns the user's most frequently watched genre as a string.
def user_most_watched_genre(user_data):
    user_movies = user_data["watched"]
    genre_list = []
    mode = None

    for movie in user_movies:
        movie_genre = movie["genre"]
        if movie_genre == []:
            return None
        genre_list.append(movie_genre)
        mode = statistics.mode(genre_list)

    return mode


def get_rec_from_favorites(user_data):
    rec_movies = []
    user_fav_list = user_data["favorites"]
    friends_watched = compiled_friends_watched(user_data)

    for index in range(len(user_fav_list)):
        if user_fav_list[index] not in friends_watched:
            rec_movies.append(user_fav_list[index])

    return rec_movies