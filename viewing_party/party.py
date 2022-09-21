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
def get_watched_avg_rating(user_data):
  rating_list = []
  average = 0.0
  for movie_list in user_data["watched"]:
    if len(movie_list) != 0:
      rating_list.append(movie_list["rating"])
      rating_sum = sum(rating_list)
      count_of_ratings = len(rating_list)
      average = rating_sum / count_of_ratings
  
    else:
      return average
  return average


def get_most_watched_genre(user_data):
  genres_list = []
  genres_dict = {}
  count = 0
  for movie_list in user_data["watched"]:
    if len(movie_list) != 0:
      genre_title = movie_list["genre"]   
      if genre_title in genres_list:
        count += 1
        genres_dict[count] = count
      else:
        genres_list.append(genre_title)
        genres_dict[genre_title] = 1
      
        return genres_list[0]
        
    return None
      
  

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------