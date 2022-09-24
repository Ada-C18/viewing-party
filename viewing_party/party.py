# ------------- WAVE 1 --------------------

from symbol import subscriptlist


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

def watch_movie(user_data, title):
  for movie in user_data["watchlist"]:
    if movie['title'] == title:
      user_data["watched"].append(movie)
      user_data["watchlist"].remove(movie)

  return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
  movies_watched = user_data["watched"]
  length = len(movies_watched)
    
  total = 0

  for ratings in movies_watched:
    total += float(ratings["rating"])
    average = total / length
  if length == 0:
    return 0
  
  return average

def get_most_watched_genre(user_data):
  movies = user_data["watched"]
  genres = {}

  for movie_watched in movies:
    genre = movie_watched["genre"]
    if genre not in genres:
      genres[genre] = 1
    else :
      genre in genres
      genres[genre] += 1
  if len(movies) == 0:
    return None
  
  most_watched_times = 1
  most_watched_genre = ""
  
  for genre, watched_times in genres.items():
    if watched_times > most_watched_times:
      most_watched_times = watched_times
      most_watched_genre = genre
  return most_watched_genre
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
  users_watched = user_data.get('watched', [])
  friends = watched_by_friends(user_data)
  unique_list = []

  for movie in users_watched:
    if movie not in friends:
      unique_list.append(movie)

  return unique_list

def watched_by_friends(user_data):
  friends_list = []
  for friend in user_data['friends']:
    friends_list.extend(friend['watched'])

  return friends_list 
def remove_duplicates_by_title(movie_list):
  movie_dict = {}
  for movie in movie_list:
    if movie['title'] not in movie_dict:
      movie_dict[movie['title']] = movie 

  return list(movie_dict.values())


def get_friends_unique_watched(user_data):

  friends = watched_by_friends(user_data)
  user_watched = user_data.get('watched', [])
  not_unique = []

  for movie in friends:
    if movie not in user_watched:
      not_unique.append(movie)

  unique = remove_duplicates_by_title(not_unique)

  return unique

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
  movies_not_watched= get_friends_unique_watched(user_data)
  recommended_movies = []
  subscription =user_data["subscriptions"]

  for movies in movies_not_watched:
    if movies["host"] in subscription:
      recommended_movies.append()
  return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
  recommended_movies =[]
  genre =get_most_watched_genre(user_data)

  for movie_not_watched in get_friends_unique_watched(user_data):
    if movie_not_watched["genre"] in genre:
      recommended_movies.append(movie_not_watched)

  return recommended_movies