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

janes_data = {
        "watchlist": [{
            "title": MOVIE_TITLE_1,
            "genre": GENRE_1,
            "rating": RATING_1
        }],
        "watched": []
    }
def watch_movie(user_data, title):
    for i in range(len(user_data["watchlist"])):
        if title in (user_data["watchlist"][i]["title"]):
        # if (user_data["watchlist"][i]["title"]) == title:
            watched_movie = (user_data["watchlist"].pop(i))
            user_data["watched"].append(watched_movie)
    # updated_data = user_data
    print(user_data)
watch_movie(janes_data, MOVIE_TITLE_1)


# print("\n-----Wave 02 user_data-----")
# pp.pprint(clean_wave_2_data())



# print("\n-----Wave 03 user_data-----")
# pp.pprint(clean_wave_3_data())

# Wave 04 user data
# print("\n-----Wave 04 user_data-----")
# pp.pprint(clean_wave_4_data())



# Wave 05 user data
# print("\n-----Wave 05 user_data-----")
# pp.pprint(clean_wave_5_data())

