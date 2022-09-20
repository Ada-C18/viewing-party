# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_move = {"title": title,
                "genre" : genre,
                "rating": rating}
    for key, value in new_move.items():
        if value == None:
            return None
    else:
        return new_move

def add_to_watched(user_data, movie):
  user_data = {"watched":[movie]}
  return user_data

def add_to_watchlist(user_data,movie):
  user_data = {"watchlist":[movie]}
  return user_data
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

