# ------------- WAVE 1 --------------------
# -----------------------------------------

from viewing_party.party import *
from dataclasses import dataclass
#from symbol import subscript
from xml.dom import UserDataHandler


def create_movie(title, genre, rating):
    movie_dictionary = {}
    if title and genre and rating:
        movie_dictionary["title"] = title
        movie_dictionary["genre"] = genre
        movie_dictionary["rating"] = rating
        return movie_dictionary

    else:
        return None

def add_to_watched(user_data, movie):

    user_data["watched"].append(movie)
    return user_data
#"watched": [{"title": "{movie} "genre": "Horror", "rating": 3.5},
          #  {"title": "Title A", "genre": "Horror", "rating": 3.5},
           # {"title": "Title A", "genre": "Horror", "rating": 3.5}]

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == title:
            del user_data["watchlist"][i]
            user_data["watched"].append(title)
            return user_data

        else:
            return user_data



# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    average = 0
    sum = 0
    if len(user_data["watched"]) != 0:
        for i in range(len(user_data["watched"])):
            sum += user_data["watched"][i]["rating"] 
        average = sum /len(user_data["watched"])
        return average
    else: 
        average = 0
        return average

    #2
def get_most_watched_genre(user_data):
	genremostwatched = {}
	if len(user_data["watched"]) == 0:
		return None
	else:

		for i in range (len(user_data["watched"])):

			if user_data["watched"][i]["genre"] in genremostwatched.keys():

				genremostwatched[user_data["watched"][i]["genre"]] += 1
			else:
				
				genremostwatched[user_data["watched"][i]["genre"]] = 1
		max_genre = max(genremostwatched)
		return max_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    movies_watch_with_friends = []

    for i in range(len(user_data["watched"])):

        for j in range(len(user_data["friends"])):

            if user_data["watched"][i]["title"] == user_data["friends"][0]["watched"][j]["title"]:

                if user_data["watched"][i]["title"] not in movies_watch_with_friends:
                        movies_watch_with_friends.append(user_data["friends"][j])

    return movies_watch_with_friends

def get_friends_unique_watched(user_data):
    friends_watched = []
    user_watched = []
    unique_watched = []

    for i in range (len(user_data["friends"])):
        for j in user_data["friends"][i]["watched"]:
            friends_watched.append(j["title"])

    for i in user_data["watched"]:
            user_watched.append(i["title"])
    for i in user_watched:
            if i in friends_watched:
                friends_watched.remove(i)
    for i in range(len(user_data["friends"])):
        for j in user_data["friends"][i]["watched"]:
            if j["title"] in friends_watched and j["title"] not in unique_watched:
                unique_watched.append(j)
    return unique_watched
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

    for i in range(len(user_data["watched"])):#

        for j in range(len(user_data["friends"])):

            for k in range(len(user_data["subscriptions"])):

                if user_data["watched"][i]["title"] and not user_data["friends"][0]["watched"][j]["title"] and user_data["friends"][0]["watched"][j]["host"] == user_data["subscriptions"][k]:

                    recommended_movies.append(user_data["watched"][j]["title"])

    return recommended_movies




# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    recommended_movies = []
    most_frequently = get_most_watched_genre(user_data)
    
    for i in range(len(user_data["watched"])):

        for j in range(len(user_data["friends"])):

            if user_data["watched"][i]["genre"] != most_frequently and user_data["friends"][0]["watched"][j]["genre"] == most_frequently:
                recommended_movies.append(user_data["watched"][j]["title"])

    return recommended_movies

def get_rec_from_favorites(user_data):
    list_of_recommended_movies = []
    for j in range(len(user_data["friends"])):
        for k in range(len(user_data["favorites"])):
            if user_data["friends"][0]["watched"][j]["title"] == user_data["favorites"][k]["title"]:
                list_of_recommended_movies.append(user_data["favorites"][k])
    return list_of_recommended_movies
    



