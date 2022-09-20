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

# user data = {
#   "watchlist": [{movie:move, genre: genre}]
# }
janes_data = clean_wave_2_data()
def get_most_watched_genre(user_data):
    genre_list = []
    genre_counter = {}
    for i in range(len(user_data["watched"])):
        genre_list.append(user_data["watched"][i]["genre"])
    for genre in genre_list:
        if genre not in genre_counter:
            genre_counter[genre] = 1
        elif genre in genre_counter:
            genre_counter[genre] += 1
    max_value = max(genre_counter.values())
    for key, value in genre_counter.items():
        if max_value == value:
            return key


        # if genre in genre_counter.keys():
        #     genre_counter["genre"] += 1
        # elif genre not in genre_counter.keys():
        #     genre_counter["genre"] = 1
    # print(genre_counter)
    # should be 3 fantasy, 1 action, 2 intrigue



get_most_watched_genre(janes_data)

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

user_data = clean_wave_5_data()
def get_new_rec_by_genre(user_data):
    # get users most frequent genre
    # user_most_frequent_genre = get_most_watched_genre(user_data)
    recs = []
    # add to movie rec if
        # user has not watched it
        # friend HAS watched
    friend_has_watched = get_friends_unique_watched(user_data)
        # genre of movie is same as user's most frequent
    # output is list of rec movies
    # print(user_most_frequent_genre)
    print(friend_has_watched)

# get_new_rec_by_genre(user_data)