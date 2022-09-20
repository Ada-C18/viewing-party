# ------------- WAVE 1 --------------------
from lib2to3.pytree import generate_matches
# from turtle import title

def create_movie(title, genre, rating):
    new_movie = { }
    
    if title == None or genre == None or rating == None:
        return None

    else:
        new_movie['title'] = title
        new_movie['genre'] = genre
        new_movie['rating'] = rating
    
        return new_movie
    

def add_to_watched(user_data,movie):
    
    user_data['watched'].append(movie)
    
    return user_data
    
def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    
    return user_data

def watch_movie(user_data, title):

    """
    title = 'string'
    input : user_data = dictionary
            2 keys, 'watchlist', 'watched'
            values = [ list ]
    """
    
    for count in range(len(user_data['watchlist'])):
        if user_data["watchlist"][count]['title'] == title:
            
            user_data['watched'].append(user_data["watchlist"][count])
            
            del user_data['watchlist'][count]
        
    return user_data         


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    sum = 0
    count = 0
    for count in range(len(user_data['watched'])):
        if (user_data["watched"][count]['rating']) != 0:
            sum += (user_data["watched"][count]['rating'])
        
        else:
            user_data["watched"][count]['rating'] = 0.0
            sum += (user_data["watched"][count]['rating'])

    average = sum / (count+1)
    return average

def get_most_watched_genre(user_data):
    total_genre = {}

    if user_data["watched"] == []:
        max_genre = None
    else:
        for count in range(len(user_data['watched'])):
            if user_data["watched"][count]['genre'] not in total_genre:
                total_genre[user_data["watched"][count]['genre']] = 1
            else:
                total_genre[user_data["watched"][count]['genre']] +=1
        max_genre = max(total_genre, key=total_genre.get)
    return max_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    movies_user = []
    # friends_user = []
    
    # missing_list = []
    # print('watch>>>',user_data)

    for count in range(len(user_data['watched'])):
        i = 0
        # for movies in (user_data['friends']['counter'])):
        print(count,'>>', user_data['watched'][count]['title'])
        print(count, '>>, user_data['friends'][i]['watched']['title'])
    
    #     if user_data['watched'][count]['title'] not in user_data['friends'][i]['watched']['title']:
    #         movies_user.append(user_data['watched'][count])
    #     i +=1
        
    # return movies_user    
            
        
        
    #     # print('count', count)
    #     # print('len>>>', len(user_data['watched']))
        
    #     print('prueba watch>>>', user_data['watched'][count]['title'] )
    #     # print('prueba friends>>>', user_data['friends'] )
    #     
    # 
    #     for count2 in range(len(user_data['friends'])):
    #         print('len 2>>>>', len(user_data['friends']))
    #         print('count 2>>>>', count2)
    #         print('prueba friend 2>>>',user_data['friends'][count2]['watched'])
            
    #         for count3 in range(len(user_data['friends'][count2]['watched'])):
    #             print('len 3>>>>', len(user_data['friends'][count2]['watched']))
    #             print('count 3>>>>', count3)
    #             print('prueba friend 3>>>',user_data['friends'][count2]['watched'][count3]['title'])
                
    #             if user_data['friends'][count2]['watched'][count3]['title'] ==  user_data['watched'][count]['title']:
    #                 break
    #             else:
    #                 missing_list.append(user_data['watched'][count]['title'])
                
    # print(missing_list)
    #     # print(len(user_data['friends'])
    


        # for count in range(len(user_data['friends'])):
        #     print('number>>', count)
        #     # print('prueba friends>>', user_data['friends']['watched'][count]['title'] )
        
#     for count in range(len('watched'])):
        
#         print(user_data['friends'])
        
        # if user_data['watched'][count]['title'] in user_data['friends']['watched'][count]['title']:
        #     print('prueba user', user_data['watched'][count]['title'] )
        #     print('prueba friends', user_data['friends']['watched'][count]['title'])
        
        # for movies in user_data['watched'][count]['title']:
        #     print('movies>>>', movies)
    
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------