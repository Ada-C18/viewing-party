# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {}

    if title == False or title == None:
        return None
    if genre == False or genre == None:
        return None
    if rating == False or rating == None:
        return None

    new_movie["title"] = title
    new_movie["genre"] = genre
    new_movie["rating"] = rating

    return new_movie

def add_to_watched(user_data, movie):
    if movie is not False:
        user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    if movie is not False:
        user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):
    to_watch = len(user_data["watchlist"])
    movie_index = 0
    
    while movie_index < to_watch:
        if user_data["watchlist"][movie_index]["title"] == title:
            del user_data["watchlist"][movie_index]
            user_data["watched"].append(title)
        movie_index += 1

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    starting_avg = 0.0
        
    ratings_list = []
    deets = 0
    watched_movies = len(user_data['watched'])

    while deets < watched_movies:
        new_rating = user_data['watched'][deets]['rating']
        ratings_list.append(new_rating)
        deets += 1
    
    for x in ratings_list:
        starting_avg = float(starting_avg + x)

    final_avg = None

    if len(ratings_list) == 0:
        return starting_avg
    else:
        compute_avg = starting_avg/len(ratings_list)
        return compute_avg

def get_most_watched_genre(user_data):
    if user_data['watched'] == []:
        return None
    
    all_genres_list = []
    deets = 0
    watched_movies = len(user_data['watched'])

    while deets < watched_movies:
        genre = user_data['watched'][deets]['genre']
        all_genres_list.append(genre)
        deets += 1
    
    most_watched_dict = {}

    for genre in all_genres_list:
        most_watched_dict[genre] = 0

    for gawnruhs in most_watched_dict.keys():
        real_count = all_genres_list.count(gawnruhs)
        most_watched_dict[gawnruhs] = real_count

    most_watched_genre = None
    num_watched = 0

    for g in most_watched_dict.keys():
        if most_watched_dict[g] > num_watched:
            most_watched_genre = g
            num_watched = most_watched_dict[g]
    
    return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    orig = len(user_data['watched'])
    user = 0

    compile_friends = []
    x = 0

    while x < len(user_data['friends']):
        for movies in user_data['friends'][x].values():
            compile_friends.append(movies)
        x += 1

    unpack_movies = []
    y = 0

    while y < len(compile_friends):
        z = 0
        while z < len(compile_friends[y]):
            unpack_movies.append(compile_friends[y][z])
            z += 1
        y += 1

    original_list = []
    runner = 0

    while runner < orig:
        if user_data['watched'][runner] not in unpack_movies:
            original_list.append(user_data['watched'][runner])
        runner += 1

    return original_list

def get_friends_unique_watched(user_data):
    orig = len(user_data['watched'])
    user = 0

    compile_friends = []
    x = 0

    while x < len(user_data['friends']):
        for movies in user_data['friends'][x].values():
            compile_friends.append(movies)
        x += 1

    unpack_friends_movies = []
    y = 0

    while y < len(compile_friends):
        z = 0
        while z < len(compile_friends[y]):
            unpack_friends_movies.append(compile_friends[y][z])
            z += 1
        y += 1

    unpack_user_movies = []
    a = 0

    while a < len(user_data['watched']):
        unpack_user_movies.append(user_data['watched'][a])
        a += 1

    friends_originals = []
    runner = 0

    while runner < len(unpack_friends_movies):
        if unpack_friends_movies[runner] in unpack_user_movies:
            pass
        else:
            if unpack_friends_movies[runner] in friends_originals:
                pass
            else:
                friends_originals.append(unpack_friends_movies[runner])
        runner += 1

    return friends_originals
    
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    potential_recs = get_friends_unique_watched(user_data)

    recs_could_watch = []
    x = 0

    while x < len(potential_recs):
        if potential_recs[x]['host'] in user_data['subscriptions']:
            recs_could_watch.append(potential_recs[x])
        x += 1
    
    return recs_could_watch

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    user_fave_genre = get_most_watched_genre(user_data)

    potential_recs = get_friends_unique_watched(user_data)

    recs_user_might_like = []
    x = 0

    while x < len(potential_recs):
        if potential_recs[x]['genre'] == user_fave_genre:
            recs_user_might_like.append(potential_recs[x])
        x += 1
    
    return recs_user_might_like

def get_rec_from_favorites(user_data):
    user_faves = user_data['favorites']

    unique_user_movies = get_unique_watched(user_data)

    user_recs = []
    x = 0

    while x < len(unique_user_movies):
        if unique_user_movies[x] in user_faves:
            user_recs.append(unique_user_movies[x])
        x += 1

    return user_recs