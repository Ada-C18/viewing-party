# import source code
from collections import Counter
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



#print("\n-----Wave 03 user_data-----")
#pp.pprint(clean_wave_3_data())

# Wave 04 user data
# print("\n-----Wave 04 user_data-----")
# pp.pprint(clean_wave_4_data())



# Wave 05 user data
#print("\n-----Wave 05 user_data-----")
#pp.pprint(clean_wave_5_data())
sonyas_data = clean_wave_5_data()
# print(sonyas_data["friends"])
def get_rec_from_favorites(user_data):

    user_fav_movies = []
    friend_watched_list = []
    recs = []

    for movie in user_data["favorites"]:
        user_fav_movies.append(movie)

    for friend_movie in user_data['friends']:
        for movie in friend_movie['watched']:
            friend_watched_list.append(movie)

    for fav_movie in user_fav_movies:
        if fav_movie not in friend_watched_list:
            recs.append(fav_movie)
    return recs

    # print(user_data["favorites"])
    # friends_watched = []
    # recs = []
    # for i in range(len(user_data["friends"])):
    #     friends_watched.append(user_data["friends"][i]["watched"])
    # print(friends_watched)
    # for i in range(len(user_data["favorites"])):
    #     if user_data["favorites"][i] not in friends_watched:
    #         recs.append(user_data["favorites"][i])
    # print(recs)
get_rec_from_favorites(sonyas_data)
#     recs_from_favorites = []
#     friends_have_not_watched = get_unique_watched(user_data)
# # Determine a list of recommended movies. A movie should be added to this list if and only if:
# # The movie is in the user's "favorites"
# # None of the user's friends have watched it
#     # loop through favorites and if not add
#     for favs in user_data["favorites"]:
#         for movies in friends_have_not_watched:
#             if favs != movies:
#                 recs_from_favorites.append(favs)
#     print(recs_from_favorites)
   

# get_rec_from_favorites(sonyas_data)