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
    title_dict={}
    for entry in user_data["watched"]:
        title_dict[entry["title"]]=entry
    user_watched=set(key for key in title_dict.keys())
    friends_title_dict={}
    for count in user_data["friends"]:
        for entry in count["watched"]:
            friends_title_dict[entry["title"]]=entry
    friends_watched=set(key for key in friends_title_dict.keys())
    title_list=list(user_watched.difference(friends_watched))
    movie_list=[title_dict[title] for title in title_list]
    return movie_list
    #friends_watched={entry["title"] for entry in user_data["friends"]}
def get_friends_unique_watched(user_data):
    title_dict={}
    for entry in user_data["watched"]:
        title_dict[entry["title"]]=entry
    user_watched=set(key for key in title_dict.keys())
    friends_title_dict={}
    for count in user_data["friends"]:
        for entry in count["watched"]:
            friends_title_dict[entry["title"]]=entry
    friends_watched=set(key for key in friends_title_dict.keys())
    title_list=list(friends_watched.difference(user_watched))
    movie_list=[friends_title_dict[title] for title in title_list]
    return movie_list


        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

