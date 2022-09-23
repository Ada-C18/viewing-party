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

janes_data = {
    "watchlist": [FANTASY_1],
    "watched": [FANTASY_2, HORROR_1, ACTION_1, FANTASY_1, FANTASY_2, HORROR_1, ACTION_1, FANTASY_1]
    }

    # Act
#updated_data = get_most_watched_genre(janes_data)

#print(updated_data)
#print(updated_data)

# print("\n-----Wave 02 user_data-----")
# pp.pprint(clean_wave_2_data())

# print("\n-----Wave 03 user_data-----")
# #pp.pprint(clean_wave_3_data())

# wave_3_user_data = clean_wave_3_data()
#print(wave_3_user_data)
# new_data = get_friends_unique_watched(wave_3_user_data)
# print(new_data)
# Wave 04 user data
# print("\n-----Wave 04 user_data-----")
# pp.pprint(clean_wave_4_data())
# get_available_recs(clean_wave_4_data())
# # Wave 05 user data
print("\n-----Wave 05 user_data-----")
pp.pprint(clean_wave_5_data())
