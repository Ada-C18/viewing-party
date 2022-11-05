# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    
    movie_dict = {"title": title, "genre": genre, "rating": rating}
    return movie_dict

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    new_watchlist_list = user_data["watchlist"]
    new_watchlist_list.append(movie)
    user_data["watchlist"] = new_watchlist_list
    return user_data

def watch_movie(user_data, title): 
    for movie in list(user_data["watchlist"]):
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            break

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    watched_movies_list = user_data["watched"]
    if len(watched_movies_list) == 0:
        return 0.0
    sum_of_ratings = 0
    for movie in watched_movies_list:
        movie_rating = movie["rating"]
        sum_of_ratings+= movie_rating
    
    return sum_of_ratings/len(watched_movies_list)

def get_most_watched_genre(user_data):
    watched_movies_list = user_data["watched"]
    if len(watched_movies_list) == 0:
        return None
    #create a dictionary containing frequency of each genre
    genre_freq = {}
    for movie in watched_movies_list:
        movie_genre = movie["genre"]
        if movie_genre not in genre_freq:
            genre_freq[movie_genre] = 1
        else:
            genre_freq[movie_genre] += 1
        
    #initially I used this code to find the most frequent genre using the values of the dictionary (which represents the freqnecy), and figuring out the key. But commented it out bc I found a one liner online to make it shorter.
    #list_of_popular_genres = []
    #max_frequency = 0
    #for genre in genre_freq:
    #    if genre_freq[genre] > max_frequency:
    #        max_frequency = genre_freq[genre]
    #        list_of_popular_genres.append(genre)
    #return list_of_popular_genres[-1] 

    return max(genre_freq, key=genre_freq.get)
    
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    list_of_titles_watched_by_friends = []
    for friend in user_data["friends"]:
          for movie in friend["watched"]:
            list_of_titles_watched_by_friends.append(movie["title"])

    list_of_titles_watched_by_user = []
    for movie in user_data["watched"]:
        list_of_titles_watched_by_user.append(movie["title"])
    
    #using sets to find the difference!
    set_of_friends_movies = set(list_of_titles_watched_by_friends)
    set_of_users_movies = set(list_of_titles_watched_by_user)
    set_of_movies_watched_by_user_only = set_of_users_movies - set_of_friends_movies

    list_of_unique_movies_watched = []

    #for each movie in the user's watched list, if the title appears in the 
    #set of unique movies, then we add it to the list we intend to return
    for movie in user_data["watched"]:
        if movie["title"] in set_of_movies_watched_by_user_only:
            list_of_unique_movies_watched.append(movie)

    return list_of_unique_movies_watched

def get_friends_unique_watched(user_data):
    list_of_titles_watched_by_friends = []
    for friend in user_data["friends"]:
          for movie in friend["watched"]:
            list_of_titles_watched_by_friends.append(movie["title"])

    list_of_titles_watched_by_user = []
    for movie in user_data["watched"]:
        list_of_titles_watched_by_user.append(movie["title"])
    
    #using sets to find the difference!
    set_of_friends_movies = set(list_of_titles_watched_by_friends)
    set_of_users_movies = set(list_of_titles_watched_by_user)
    set_of_movies_watched_by_friends_only = set_of_friends_movies - set_of_users_movies 

    list_of_unique_movies_watched = []

    #for each friend, and each movie in their list, if the title appears in the 
    #set of unique movies, then we add it to the list we intend to return
    for friend in user_data["friends"]:
          for movie in friend["watched"]:
            if movie["title"] in set_of_movies_watched_by_friends_only and movie not in list_of_unique_movies_watched:
                list_of_unique_movies_watched.append(movie)

    return list_of_unique_movies_watched

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recommended_movies = []
    list_of_movies_watched_by_atleast_one_friend_but_not_user = get_friends_unique_watched(user_data)
    for movie in list_of_movies_watched_by_atleast_one_friend_but_not_user:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)
    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    recommended_movies = []
    list_of_movies_watched_by_atleast_one_friend_but_not_user = get_friends_unique_watched(user_data)
    most_watched_genre = get_most_watched_genre(user_data)
    for movie in list_of_movies_watched_by_atleast_one_friend_but_not_user:
        if movie["genre"] == most_watched_genre:
            recommended_movies.append(movie)
    return recommended_movies

def get_rec_from_favorites(user_data):
    recommended_movies = []
    list_of_movies_watched_by_user_but_not_friends = get_unique_watched(user_data)
    for movie in user_data["favorites"]:
        for unique_movie in list_of_movies_watched_by_user_but_not_friends:
            if unique_movie["title"] == movie["title"]:
                recommended_movies.append(movie)
    
    return recommended_movies
