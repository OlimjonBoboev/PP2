movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

# Function to check if a movie has an IMDB score above 5.5
def is_highly_rated(movie):
    return movie["imdb"] > 5.5

# Function to return movies with an IMDB score above 5.5
def highly_rated_movies(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]

# Function to return movies under a given category
def movies_by_category(movies, category):
    return [movie for movie in movies if movie["category"].lower() == category.lower()]

# Function to compute the average IMDB score of a list of movies
def average_imdb_score(movies):
    if not movies:
        return 0  # Return 0 if the list is empty
    return sum(movie["imdb"] for movie in movies) / len(movies)

# Function to compute the average IMDB score for a given category
def average_imdb_score_by_category(movies, category):
    category_movies = movies_by_category(movies, category)
    return average_imdb_score(category_movies)

# Example Usage
print(is_highly_rated(movies[0]))  # True
print(highly_rated_movies(movies))  # List of movies with IMDB > 5.5
print(movies_by_category(movies, "Romance"))  # List of Romance movies
print(average_imdb_score(movies))  # Average IMDB score of all movies
print(average_imdb_score_by_category(movies, "Romance"))  # Average IMDB score of Romance movies
