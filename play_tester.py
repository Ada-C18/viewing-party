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

# print(create_movie("title1", "genre1", "rathing1"))
# print(add_to_watched("stacy", )
# janes_data = {
#     "watchlist": [{
#         "title": MOVIE_TITLE_1,
#         "genre": GENRE_1,
#         "rating": RATING_1
#     }],
#     "watched": []
# }
# watch_movie(janes_data, MOVIE_TITLE_1)

# {"title":"Shrek", "genre": "Family", "rating": 4.5})

# print("\n-----Wave 02 user_data-----")
# pp.pprint(clean_wave_2_data())
# print(get_most_watched_genre(clean_wave_2_data))

# print("\n-----Wave 03 user_data-----")
#pp.pprint(clean_wave_3_data())
# get_unique_watched(clean_wave_3_data())
# print(get_friends_unique_watched(clean_wave_3_data()))

# Wave 04 user data
# print("\n-----Wave 04 user_data-----")
#pp.pprint(clean_wave_4_data())
# print(get_available_recs(clean_wave_4_data()))

# Wave 05 user data
print("\n-----Wave 05 user_data-----")
#pp.pprint(clean_wave_5_data())
print(get_rec_from_favorites(clean_wave_5_data()))