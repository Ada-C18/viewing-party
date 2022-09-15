def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        print("Missing title, genre or rating")
        return None
    movie_dict={
        "title":title,
        "genre":genre,
        "rating":rating
    }
    return movie_dict
def add_to_watched(user_data,movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data,movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data,title):
    for count in range(len(user_data["watchlist"])):
        if title == user_data["watchlist"][count]["title"]:
            user_data["watched"].append(user_data["watchlist"].pop(count))
            break
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
import collections

def get_watched_avg_rating(user_data):
    sum=0.0
    if len(user_data["watched"])<1:
        return sum
    for entry in user_data["watched"]:
        sum+=entry["rating"]
    return sum/len(user_data["watched"])
def get_most_watched_genre(user_data):
    if len(user_data["watched"])<1:
        return None
    genre_list=[]
    for entry in user_data["watched"]:
        genre_list.append(entry["genre"])
    counted=collections.Counter(genre_list)
    return counted.most_common()[0][0]





# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    user_watched={entry["title"] for entry in user_data["watched"]}
    friends_watched=[]
    for entry in user_data["friends"][0]:
        friends_watched.append(entry["title"])
    print(friends_watched)
    #friends_watched={entry["title"] for entry in user_data["friends"]}
    """titles = user_watched.difference(friends_watched)
    print(user_watched, friends_watched, titles)
    return_list_of_dicts=[]
    for entry in user_data["watched"]:
        if entry["title"] in titles:
            return_list_of_dicts.append(entry)
    return return_list_of_dicts"""

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

