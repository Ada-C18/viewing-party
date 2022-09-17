# ------------- WAVE 1 --------------------
# 1. Create a function named  `create_movie`. This function and all subsequent functions should be in `party.py`. `create_movie` should...
# - take three parameters: `title`, `genre`, `rating`
# - If those three attributes are truthy, then return a dictionary. This dictionary should...
#   - Have three key-value pairs, with specific keys
#   - The three keys should be `"title"`, `"genre"`, and `"rating"`
#   - The values of these key-value pairs should be appropriate values
# - If `title` is falsy, `genre` is falsy, or `rating` is falsy, this function should return `None`

def create_movie(title, genre, rating):
    if title and genre and rating:
        movie_dict = {}
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
        return movie_dict
    return None

# 2. Create a function named `add_to_watched`. This function should...

# - take two parameters: `user_data`, `movie`
#   - the value of `user_data` will be a dictionary with a key `"watched"`, and a value which is a list of dictionaries representing the movies the user has watched
#     - An empty list represents that the user has no movies in their watched list
#   - the value of `movie` will be a dictionary in this format:
#     - ```python
#       {
#         "title": "Title A",
#         "genre": "Horror",
#         "rating": 3.5
#       }
#       ```
# - add the `movie` to the `"watched"` list inside of `user_data`
# - return the `user_data`



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

