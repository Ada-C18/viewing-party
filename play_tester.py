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

def get_friends_unique_watched(user_data):
# return what their friends have watched but not user
    user_watched_list = []
    friend_watched_list = []
    friend_unique_movies = []

    for movie in user_data["watched"]:
        user_watched_list.append(movie)

    for friend_movie in user_data['friends']:
        for movie in friend_movie['watched']:
            friend_watched_list.append(movie)

    for i in friend_watched_list:
        if i not in user_watched_list:
            friend_unique_movies.append(i)
    return friend_unique_movies
    
# Wave 04 user data
#print("\n-----Wave 04 user_data-----")
#pp.pprint(clean_wave_4_data())

# Wave 05 user data
#print("\n-----Wave 05 user_data-----")
#pp.pprint(clean_wave_5_data())
