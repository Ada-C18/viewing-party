"""
This is a module that contains the helper functions implemented in the 
viewing-party project (party.py file).
"""

from viewing_party.party import *
from tests.test_constants import *

def build_user_movie_list(user_data):
    user_watched_movie_list = []
    for movie in user_data["watched"]:
        user_watched_movie_list.append(movie)
    return user_watched_movie_list

def build_friend_movie_list(user_data):
    friends_watched_movie_list = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_movie_list.append(movie)
    return friends_watched_movie_list