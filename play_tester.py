# import source code
from viewing_party.party import *

# import test data
from tests.test_constants import *

# import "pretty-print" library
import pprint
pp = pprint.PrettyPrinter(indent=4)

# play testing section
# print("\n-----Wave 01 test data-----")
# pp.pprint(HORROR_1)
# pp.pprint(FANTASY_1)
# pp.pprint(FANTASY_2)

# print("\n-----Wave 02 user_data-----")
# pp.pprint(clean_wave_2_data())

# def get_watched_avg_rating(janes_data):
#     avg_rating = 0
#     rating_sum = 0
#     for key in janes_data["watched"]:
#         all_ratings = []
#         if key == "rating":
#             all_ratings.append(key)
#             rating_sum = sum(int(all_ratings))
#     avg_rating = rating_sum/len(janes_data["watched"])

#     return avg_rating

# def get_watched_avg_rating(janes_data):
#     for key in janes_data["watched"]:
#         rating_sum = 0
#         if janes_data["watched"] == "rating":
#             rating_sum = sum(int(janes_data["watched"["rating"]]))
    
#     avg_rating = rating_sum/len(janes_data)

#     print(rating_sum)

# print("\n-----Wave 03 user_data-----")
# pp.pprint(clean_wave_3_data())

# user_data = clean_wave_3_data()
# def get_unique_watched(user_data):

#     all_friends_movies = []
#     i = 0
#     for friend in user_data["friends"]:
#         for friend_movies in user_data["friends"][i]["watched"]:
#             print(friend_movies)
#             # all_friends_movies.append(friend_movies)
#         # i += 1
#         # print(friend_movies)

# get_unique_watched(user_data)

    
    # friend_list = []
    # for friend_movies in all_friends_list:
    #     friend_list.append(friend_movies["title"])

    # no_friends = []
    # for movie in user_data["watched"]:
    #     if movie["title"] not in friend_list:
    #         no_friends.append(movie)
    # print(no_friends)


# def get_friends_unique_watched(user_data):
#     user_data["friends"][0]["watched"].append(INTRIGUE_3)

#     friend_list = []

#     all_friends_list = user_data["friends"][0]["watched"] + user_data["friends"][1]["watched"]

#     seen = set()
#     clean_all_friends_list = []
#     for friend_movies in all_friends_list:
#         t = tuple(friend_movies.items())
#         if t not in seen:
#             seen.add(t)
#             clean_all_friends_list.append(friend_movies)

#     for friend_movies in clean_all_friends_list:
#         if friend_movies not in user_data["watched"]:
#             friend_list.append(friend_movies)
#     print(friend_list)

# get_friends_unique_watched(user_data)



# Wave 04 user data
# print("\n-----Wave 04 user_data-----")
# pp.pprint(clean_wave_4_data())

# user_data = clean_wave_4_data()

# def get_available_recs(user_data):

    # all_friends_movies = []
    # i = 0
    # for friend in user_data["friends"]:
    #     for friend_movies in user_data["friends"][i]["watched"]:
    #         all_friends_movies.append(friend_movies)
    #     i += 1

    # friends_watched = []
    # for friend_movies in all_friends_movies:
    #     if friend_movies not in user_data["watched"]:
    #         friends_watched.append(friend_movies)

    # recomended_movies = []
    # j = 0
    # for movies in friends_watched:
    #     for subscription in user_data["subscriptions"]:
    #         if subscription in friends_watched[j]["host"]:
    #             recomended_movies.append(movies)
    #     j += 1

    # print(recomended_movies)

# get_available_recs(user_data)

from collections import Counter
# Wave 05 user data
print("\n-----Wave 05 user_data-----")
# pp.pprint(clean_wave_5_data())

user_data = clean_wave_5_data()

def get_rec_from_by_genre(user_data):

    if len(user_data["watched"]) == 0:
        return []

    user_genre = []   
    for user_movies in user_data["watched"]:
        user_genre.append(user_movies["genre"])
        genre_count = Counter(user_genre)
        user_freq_genre = genre_count.most_common(1)[0][0]

    all_friends_movies = []
    i = 0
    for friend in user_data["friends"]:
        for friend_movie in user_data["friends"][i]["watched"]:
            all_friends_movies.append(friend_movie)
        i += 1

    user_not_watched = []
    for friends_movies in all_friends_movies:
        if friends_movies not in user_data["watched"]:
            user_not_watched.append(friends_movies)

    recommended_movies = []
    i = 0
    for movie in user_not_watched:
        if user_freq_genre in user_not_watched[i]["genre"]:
            recommended_movies.append(movie)
        i += 1

    if len(user_data["watched"]) == 0:
        recommended_movies = []


    print(recommended_movies)

def get_rec_from_favorites(user_data):

    all_friends_movies = []
    i = 0
    for friend in user_data["friends"]:
        for friend_movie in user_data["friends"][i]["watched"]:
            all_friends_movies.append(friend_movie)
        i += 1

    friend_titles = []
    for friend_movie in all_friends_movies:
        friend_titles.append(friend_movie["title"])

    friends_not_watched = []
    for user_movie in user_data["favorites"]:
        if user_movie["title"] not in friend_titles:
            friends_not_watched.append(user_movie)
    print(friends_not_watched)




get_rec_from_favorites(user_data)