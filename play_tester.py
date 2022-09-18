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

def get_available_recs(user_data):
    recs = []
    movies_from_friends = get_friends_unique_watched(user_data)
    for i in range(len(movies_from_friends)):
        if (movies_from_friends[i]['host']) in user_data['subscriptions']:
            recs.append(movies_from_friends[i])
    return recs

get_available_recs(clean_wave_4_data())

# Wave 05 user data
#print("\n-----Wave 05 user_data-----")
#pp.pprint(clean_wave_5_data())
