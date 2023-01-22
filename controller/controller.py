from model import model


def get_movie_by_title(title):
    movies = model.get_movie_by_title(title)
    return movies


def get_movies_in_year_range(from_year, to_year):
    movies = model.get_movies_in_year_range(from_year, to_year)
    result = []
    for movie in movies:
        result.append(
            {
                "title": movie['title'],
                "release_year": movie['release_year']
            }
        )

    return result


def get_data_by_rating_group(rating_group):
    if rating_group.lower() == 'children':
        rating_list = 'G'
    elif rating_group.lower() == 'family':
        rating_list = ('G', 'PG', 'PG-13')
    elif rating_group.lower() == 'adult':
        rating_list = ('R', 'NC-17')
    else:
        return f'wrong rating_group={rating_group}, ' \
               f'please select from children, family or adult'

    data = model.get_data_by_rating_group(rating_list)
    result = []
    for movie in data:
        result.append(
            {
                "title": movie['title'],
                "rating": movie['rating'],
                "description": movie['description'].strip()
            }
        )
    return result


def get_movie_by_genre(genre):
    movies = model.get_movie_by_genre(genre)
    result = []
    for movie in movies:
        result.append(
            {
                "title": movie['title'],
                "description": movie['description'].strip()
            }
        )

    return result


def get_by_type_genre_and_year(video_type, listed_in, release_year):
    movies = model.get_by_type_genre_and_year(
        video_type,
        listed_in,
        release_year
    )
    return movies
