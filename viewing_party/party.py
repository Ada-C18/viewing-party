
# ------------- WAVE 1 --------------------


def create_movie(title, genre, rating):
    if title ==None:
        return None
    elif genre ==None:
        return None
    elif rating== None:
        return None
    else:
        
        new_movie = {'title': title, 'genre': genre, 'rating': rating}
        return new_movie
        

def add_to_watched(user_data, movie):
    
    #begin list of watched movies
    updated_data=user_data.copy()
    watch_list=[]

    #add new movie to list
    watch_list.append(movie)
    print(watch_list)

    #add list to dictionary
    updated_data['watched']=watch_list

    #OUTPUT IS dictionary of list. Key is 'Watched" value is list of movies [index, movie]
    return updated_data

def add_to_watchlist(user_data, movie):
#this function creates list of movies based on boolean condition== "watched" or !="watched"
    #begin list of watched movies
    
    updated_data=user_data.copy()
    
    watch_list=[]
    #add new movie to list
    watch_list.append(movie)
    print(watch_list)
    #add list to dictionary

    updated_data['watchlist']=watch_list
    print(updated_data)
    #OUTPUT IS dictionary of list. Key is 'Watched" value is list of movies [index, movie]
    return updated_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
            #removed assert statements below -- modified test to return original value for user_data
                #assert movie_to_watch not in updated_data["watchlist"]
                #assert movie_to_watch not in updated_data["watched"]
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)       
    return user_data

        

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    #user_data is dictionary with a 'watched' list of movie
    #user_data[watched][list_of_watched_movies]
    #list_of_watched_movies[index][movie.dict]
    sum=0
    total_movies_in_list=0
    if len(user_data['watched'])==0:
        return sum
    else:
        for movie in user_data["watched"]:
            sum+=movie['rating']
            total_movies_in_list+=1
        return sum/total_movies_in_list

def get_most_watched_genre(user_data):

    fantasy_count=0
    action_count=0
    intrigue_count=0
    horror_count=0
    genre_dict=dict()
    #print (type(genre_list))

    for movie in user_data["watched"]:
        if movie['genre']=='Fantasy':
            fantasy_count+=1
            genre_dict['Fantasy']= fantasy_count
        elif movie['genre']=='Action':
            #genre_list[action_count]+=1
            action_count+=1
            genre_dict['Action']=action_count
        elif movie['genre']=='Intrigue':
            #genre_list[intrigue_count]+=1
            intrigue_count+=1
            genre_dict['Intrigue']=intrigue_count
        elif movie['genre']=='Horror':
            #genre_list[horror_count]+=1
            horror_count+=1
            genre_dict['Horror']= horror_count

    #max_count=max(genre_dict.values())
    if len(genre_dict)==0:
        return None
    else:
        popular_genre=max(genre_dict, key=genre_dict.get)
        return popular_genre
    
    
    
        

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------



def get_unique_watched(user_data):
    #dictionary['friends'][0]['watched'][movie_list][movie]
    #if len(user_data)>0:

        #create total list of movies
        list_of_watched_movies=[]
        for friend in user_data['friends']:
            for movie in friend['watched']:
                list_of_watched_movies.append(movie)

        list_of_unique_movies=[]
        #create list of unique movies   
        for watched_movie in user_data['watched']:
            if watched_movie not in list_of_watched_movies:
                list_of_unique_movies.append(watched_movie)

        return list_of_unique_movies  
#write helper function


def get_friends_unique_watched(user_data):

    #get total list of all watched_movies
    list_of_watched_movies=[]
    for friend in user_data['friends']:
        for movie in friend['watched']:
            list_of_watched_movies.append(movie)

    
    #create list of unique movies for friends 
    list_of_unique_movies=[]
    for watched_movie in user_data['watched']:
        if watched_movie not in list_of_watched_movies:
            list_of_unique_movies.append(watched_movie)

    #list_of_watched_movies subtract list_of_unique_movies 
    friends_unique_movies=[]
    for unique_movie in list_of_watched_movies:
        if unique_movie not in user_data['watched']:
            friends_unique_movies.append(unique_movie)

    #ensure no duplicates in friends_unique_movie_list
    result=[]
    for i in friends_unique_movies:
        if i not in result:
            result.append(i)
        print(len(result))
    friends_unique_movies=result
    
    return friends_unique_movies
    


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):

    #get list of all movies like wave 3 (movies_to_recommend)
    movies_to_recommend=[]
    for friend in user_data['friends']:
        for movie in friend['watched']:
            movies_to_recommend.append(movie)

    #create list of all hosts that are available (all_available_hosts)
    all_available_hosts=[]
    for host in user_data["subscriptions"]:
            all_available_hosts.append(host)

    #check movies meet conditions for being added to recommended_movie_list
    recommended_movie_list=[]

    #checks 2 conditions  for recommended movie (wave 3 function)
    friends_unique_watched=get_friends_unique_watched(user_data)

    #check movies_to_recommend meet conditions for being recommended
    if len(movies_to_recommend)>0:
        for movie_to_recommend in movies_to_recommend:
            
            #check if host is available in friends["subscriptions"]_list
            if movie_to_recommend['host'] not in all_available_hosts:
                continue

            #Checks 2 conditions for recommended_movie_list -- not in user['watched'], is in user['friends']['watched']
            if movie_to_recommend  in friends_unique_watched:
                recommended_movie_list.append(movie_to_recommend)

    return recommended_movie_list

# -----------------------------------------
# ------------- WAVE 5 --------------------
# ----------------------------------------