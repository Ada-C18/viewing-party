# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie = {}
    if title and genre and rating: 
        movie["title"] = title
        movie["genre"] = genre 
        movie["rating"] = rating 
        return movie


def add_to_watched(user_data, movie):
    user_data = {}
    user_data["watched"] = [movie]
    return user_data


def add_to_watchlist(user_data, movie):
    user_data = {}
    user_data["watchlist"] = [movie]
    return user_data


def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:    
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data['watched'].append(movie)
            # return user_data
        
    return user_data  
# # -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    rating_list = []
    for i in range(len(user_data["watched"])):
        rating_list.append(user_data["watched"][i]["rating"])
    # if len(rating_list) != 0:
    if rating_list:
        average = sum(rating_list)/len(rating_list)
    else:
        average = 0.0
    return average 


def get_most_watched_genre(user_data):
    genre_list = []
    for i in range(len(user_data["watched"])):
        genre_list.append(user_data["watched"][i]["genre"])
    if genre_list: 
        for genre in genre_list:
            popular_genre = max(set(genre_list), key = genre_list.count)
    else: 
        popular_genre = None 
    return popular_genre
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data): 
    friends_watched_list = []
    user_watched_list = []
    unique_watched_list = []
    friends = user_data["friends"]
    user_watched = user_data["watched"]
    
    for friend in friends:
        for movie in friend["watched"]:
            friends_watched_list.append(movie["title"])
    

    for movie in user_watched:
        if movie["title"] not in friends_watched_list:  
            unique_watched_list.append(movie)
    return unique_watched_list

    

    # print(f"debug info : {friends_watched_list = },\n {user_watched_list = }") 
    # unique_watched = {}
    # friends_watched_list = []
    # user_watched_list = [] 
    # unique_watched_list = []
    # 
    
    # # for i in range(len(friend)):
    #     # for i in range(len(friend[i]["watched"])):
    #     #     friends_watched_list.append(["title"])
    # for i in range(len(friend)):
    #     for i in range(len(friend[i]['watched'])):
    #         # movie_title = [i]['watched'][i]['title']
    #         # print(movie_title)
    #         friends_watched_list.append(friend['watched'][i]["title"])
    
    # # print(f"{friends_watched_list =}")
    
    # for i in range(len(user_data["watched"])):
    #     user_watched_list.append(user_data["watched"][i]["title"])
    # # print(f"{user_watched_list =}")
    
    # for movie in user_watched_list:
    #     if movie not in friends_watched_list: 
    #         # unique_watched.update({"movie": movie})
    #         unique_watched_list.append(movie)
    
    # for movie in unique_watched_list:
    #     unique_watched['movies'] = unique_watched_list
        
    
    # print(f"debug info : {friends_watched_list = },\n {user_watched_list = },\n {unique_watched = }")        
    # print(f"{unique_watched_list = }")    
    # 

    
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

