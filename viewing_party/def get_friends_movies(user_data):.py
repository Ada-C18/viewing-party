def get_friends_movies(user_data):
    empty_list = []
    friends_watched_list_of_dicts = user_data["friends"]

    for index in range(len(friends_watched_list_of_dicts)):
        for index_2 in range(len(friends_watched_list_of_dicts[index]["watched"])):
            empty_list.append(friends_watched_list_of_dicts[index]["watched"][index_2])

    return empty_list


def get_unique_watched(user_data):
    unique_movies = []
    user_watched_list = user_data["watched"]
    friends_watched_list = get_friends_movies(user_data)

    for index in range(len(user_watched_list)):
        if not user_watched_list[index] in friends_watched_list:
            unique_movies.append(user_watched_list[index])
    
    return unique_movies


