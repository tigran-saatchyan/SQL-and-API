from model import model


def get_movie_by_title(title: str) -> dict:
    """
    Gets movie by title
    :param title:   - title for query
    :return:        - dictionary of movie arguments
    """
    movies = model.get_movie_by_title(title)
    return movies


def get_movies_in_year_range(from_year: int, to_year: int) -> list:
    """
    Get all movies in release year range
    :param from_year:   - release_year start from year
    :param to_year:     - release_year to year
    :return:            - movies between mentioned in year range
    """
    movies = model.get_movies_in_year_range(from_year, to_year)
    return movies


def get_data_by_rating_group(rating_group: str) -> list:
    """
    Gets movies by specific rating list:
        * children -  (includes only G)
        * family   -  (G, PG, PG-13)
        * adult    -  (R, NC-17)
    :param rating_group:    - rating list for query
    :return:                - list of dicts of movies
    """
    if rating_group.lower() == 'children':
        rating_list = 'G'
    elif rating_group.lower() == 'family':
        rating_list = ('G', 'PG', 'PG-13')
    elif rating_group.lower() == 'adult':
        rating_list = ('R', 'NC-17')
    else:
        return [f'wrong rating_group={rating_group} '
                f'please select from children, family or adult']

    movies = model.get_data_by_rating_group(rating_list)
    return movies


def get_movie_by_genre(genre: str) -> list:
    """
    Get all movies by specified genre
    :param genre:   - genre for query
    :return:        - list of dicts of movies
    """
    movies = model.get_movie_by_genre(genre)

    return movies


def get_most_played_with(first_actor: str, second_actor: str) -> list:
    """
    Get cast of actors played with mentioned two actors
    more than 2 times
    :param first_actor:     - first actor for query
    :param second_actor:    - second actor for query
    :return:                - movies with actors played with
    """
    cast = model.get_most_played_with(first_actor, second_actor)
    all_actors = []
    result = []

    for actors in cast:
        all_actors.extend(actors['cast'].split(', '))

    unique_actor = list(set(all_actors))
    unique_actor.remove(first_actor)
    unique_actor.remove(second_actor)

    for actor in unique_actor:
        if all_actors.count(actor) > 2:
            result.append(actor)

    return result


def get_by_type_genre_and_year(
    video_type: str,
    listed_in: str,
    release_year: int
) -> list:
    """
    Get screenplay by type, genre and release year
    :param video_type:      - screenplay type
    :param listed_in:       - screenplay genre
    :param release_year:    - screenplay release year
    :return:                - movies filtered by param's
    """
    movies = model.get_by_type_genre_and_year(
        video_type,
        listed_in,
        release_year
    )
    return movies
