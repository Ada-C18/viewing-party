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
def get_unique_watched(user_data):
  list_of_user_movies = []
  list_of_friend_movies = []
  user_has_watched_freinds_have_not_list = []
  for movie_list in user_data["watched"]:
    list_of_user_movies.append(movie_list)
  
  for friend_movie_list in user_data["friends"]:
    for watched_friend_list in friend_movie_list["watched"]:
      list_of_friend_movies.append(watched_friend_list)
  for title in list_of_user_movies:
    if title not in list_of_friend_movies:
      user_has_watched_freinds_have_not_list.append(title)
  return user_has_watched_freinds_have_not_list


def get_friends_unique_watched(user_data):
  list_of_user_movies = []
  list_of_friend_movies = []
  movies_one_of_users_freinds_have_watched_but_user_has_not = []
  
  for movie_list in user_data["watched"]:
    list_of_user_movies.append(movie_list)
  
  for friend_movie_list in user_data["friends"]:
    for watched_friend_list in friend_movie_list["watched"]:
      list_of_friend_movies.append(watched_friend_list)
  # movies_one_of_users_freinds_have_watched_but_user_has_not = []
  
  for movie in (list_of_friend_movies):
    if movie not in list_of_user_movies and len(movie) > 0:
      if movie not in movies_one_of_users_freinds_have_watched_but_user_has_not:
        movies_one_of_users_freinds_have_watched_but_user_has_not.append(movie)
      
  return movies_one_of_users_freinds_have_watched_but_user_has_not
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
  list_of_user_movies = []
  list_of_friend_movies = []
  rec_list = []
  
  for movie_list in user_data["watched"]:
    list_of_user_movies.append(movie_list)
  
  for friend_movie_list in user_data["friends"]:
    for watched_friend_list in friend_movie_list["watched"]:
      list_of_friend_movies.append(watched_friend_list)

  for movie in (list_of_friend_movies):
    if movie not in list_of_user_movies and len(movie) > 0:
      if movie not in rec_list:
        if movie["host"] in user_data["subscriptions"]:
          rec_list.append(movie)
        
  return rec_list
    

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):

  list_of_user_movies = []
  list_of_friend_movies = []
  rec_list_by_genre = [] 
  most_watched_genre = get_most_watched_genre(user_data)
  for movie_list in user_data["watched"]:
    list_of_user_movies.append(movie_list)
  
  for friend_movie_list in user_data["friends"]:
    for watched_friend_list in friend_movie_list["watched"]:
      list_of_friend_movies.append(watched_friend_list)

  for movie in (list_of_friend_movies):
    if movie not in list_of_user_movies and len(movie) > 0:
      if movie not in rec_list_by_genre:
        if movie["genre"] == most_watched_genre:
          rec_list_by_genre.append(movie)
  return rec_list_by_genre

def get_rec_from_favorites(user_data):
  list_of_user_movies = []
  list_of_friend_movies = []
  rec_list_from_fav = []
  
  for movie_list in user_data["watched"]:
    list_of_user_movies.append(movie_list)
  
  for friend_movie_list in user_data["friends"]:
    for watched_friend_list in friend_movie_list["watched"]:
      list_of_friend_movies.append(watched_friend_list)
  
  for movie in user_data["favorites"]:
    if movie not in list_of_friend_movies:
      rec_list_from_fav.append(movie)
  return rec_list_from_fav
