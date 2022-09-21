# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie = {}
    if title and genre and rating:
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
        return movie    
    else:
        return None    

def add_to_watched(user_data, movie):
    if not "watched" in user_data:
        user_data["watched"] = []
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    if not "watchlist" in user_data:
        user_data["watchlist"] = []
    user_data["watchlist"].append(movie)
    return user_data
    
def watch_movie(user_data, title):
    for ele in user_data["watchlist"]:
        if title == ele["title"]:
            user_data["watched"].append(ele)
            user_data["watchlist"].remove(ele)
            return user_data
    return user_data

janes_data = {
            "watchlist": [{
                "title": "a",
                "genre": "b",
                "rating": "c"
            }, {
                "title": "a1",
                "genre": "b1",
                "rating": "c1"
            }],
            "watched": []
        }
for ele in janes_data["watchlist"]:
    for x in ele:
        print(x)
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

