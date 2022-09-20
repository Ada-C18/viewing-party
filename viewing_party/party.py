# ------------- WAVE 1 --------------------

from optparse import TitledHelpFormatter


def create_movie(title, genre, rating):
  my_dict = {}
  title_value = bool(title)
  genre_value = bool(genre)
  rating_value = bool(rating)
  if title_value and genre_value and rating_value == True:
    my_dict["title"] = title
    my_dict["genre"] = genre
    my_dict["rating"] = rating
    return my_dict
  else:
    return None

def add_to_watched(user_data, movie):
  
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
  
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
  for movie in user_data["watchlist"]:
    if title == movie["title"]:
      user_data["watchlist"].remove(movie)

      user_data["watched"].append(movie)
      break
  return user_data
    



    
    

# }
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