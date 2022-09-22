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

print("\n-----Wave 03 user_data-----")
# pp.pprint(clean_wave_3_data())

user_data = clean_wave_3_data()
# def get_unique_watched(user_data):

#     no_friends = []
#     friend_list = []

#     all_friends_list = user_data["friends"][0]["watched"] + user_data["friends"][1]["watched"]
#     for friend_movies in all_friends_list:
#         friend_list.append(friend_movies["title"])

#     for movie in user_data["watched"]:
#         if movie["title"] not in friend_list:
#             no_friends.append(movie)
#     print(no_friends)
# get_unique_watched(user_data)

def get_friends_unique_watched(user_data):
    user_data["friends"][0]["watched"].append(INTRIGUE_3)
 
    friend_list = []

    all_friends_list = user_data["friends"][0]["watched"] + user_data["friends"][1]["watched"]

    seen = set()
    clean_all_friends_list = []
    for friend_movies in all_friends_list:
        t = tuple(friend_movies.items())
        if t not in seen:
            seen.add(t)
            clean_all_friends_list.append(friend_movies)

    for friend_movies in clean_all_friends_list:
        if friend_movies not in user_data["watched"]:
            friend_list.append(friend_movies)
    print(friend_list)




get_friends_unique_watched(user_data)



# Wave 04 user data
#print("\n-----Wave 04 user_data-----")
#pp.pprint(clean_wave_4_data())

# Wave 05 user data
#print("\n-----Wave 05 user_data-----")
#pp.pprint(clean_wave_5_data())
