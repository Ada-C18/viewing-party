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

# *****wave 1 test_inputs******
# user_data = {
#         "watchlist": [{
#             "title": MOVIE_TITLE_1,
#             "genre": GENRE_1,
#             "rating": RATING_1
#         }],
#         "watched": []
#     }

# MOVIE_TITLE_2 = "Gooneys"
# putting in own test inputs to run program to observe outputs
# print(create_movie("mybad", "horror", "4.8"))
# print(watch_movie(user_data, MOVIE_TITLE_1))
# print(watch_movie(user_data, MOVIE_TITLE_2))
# user_data = (watch_movie(user_data, MOVIE_TITLE_1))
# print(len(user_data["watchlist"]), user_data["watchlist"])
# print(len(user_data["watched"]), user_data["watched"])

# print("\n-----Wave 02 user_data-----")
# pp.pprint(clean_wave_2_data())
# **********

# *****wave 2 test_inputs******
# user_data = {"watched" :[{
#             "title": "title_a",
#             "genre": "comedy",
#             "rating": 3.9
#         }, 
#         {
#             "title": "title_b",
#             "genre": "action",
#             "rating": 3.1
#         }, 
#         {
#             "title": "title_c",
#             "genre": "comedy",
#             "rating": 5.0
#         }, 
#         {
#             "title": "title_d",
#             "genre": "horror",
#             "rating": 2.8
#         }, 
#         ]

# }
# print(get_most_watched_genre(user_data))
# ***********

print("\n-----Wave 03 user_data-----")
# pp.pprint(clean_wave_3_data())
# *****wave 3 test_inputs******
# user_data = clean_wave_3_data()

# print(get_unique_watched(user_data))

# Wave 04 user data
#print("\n-----Wave 04 user_data-----")
#pp.pprint(clean_wave_4_data())

# Wave 05 user data
#print("\n-----Wave 05 user_data-----")
#pp.pprint(clean_wave_5_data())
