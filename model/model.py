import sqlite3


def get_data(query: str) -> sqlite3.Cursor:
    """
    Connect to database and return data object
    :param query:   - query string
    :return:        - data from db
    """
    with sqlite3.connect('data/netflix.db') as con:
        con.row_factory = sqlite3.Row
        result = con.execute(query)
        return result


def get_movie_by_title(title: str) -> dict:
    """
    Gets movie by title
    :param title:   - title for query
    :return:        - dictionary of movie arguments
    """
    query = f"""
            SELECT 
                `title`, 
                `country`, 
                `release_year`, 
                `listed_in` as 'genre', 
                `description`
            FROM `netflix`
            WHERE `type` = 'Movie' AND `title` = '{title}' 
            ORDER BY `release_year` DESC
            LIMIT 1
    """
    return dict(get_data(query).fetchone())


def get_movies_in_year_range(from_year: int, to_year: int) -> list:
    """
    Get all movies in release year range
    :param from_year:   - release_year start from year
    :param to_year:     - release_year to year
    :return:            - movies between mentioned in year range
    """
    query = f"""
            SELECT 
                `title`, 
                `release_year`
            FROM `netflix`
            WHERE `type` = 'Movie' 
            AND `release_year` BETWEEN '{from_year}' AND '{to_year}' 
            ORDER BY `release_year` DESC 
            LIMIT 100
    """
    result = [dict(movie) for movie in get_data(query).fetchall()]

    return result


def get_data_by_rating_group(rating_list: tuple | str) -> list:
    """
    Gets movies by specific rating list:
        * children -  (includes only G)
        * family   -  (G, PG, PG-13)
        * adult    -  (R, NC-17)
    :param rating_list:     - rating list for query
    :return:                - list of dicts of movies
    """
    query = f"""
            SELECT 
                `title`, 
                `rating`,
                `description`
            FROM `netflix`
            """

    if len(rating_list) == 1:
        query += f"""
                WHERE `rating` = '{rating_list}'
            """
    else:
        query += f"""
                WHERE `rating` IN {rating_list}
            """
    result = [dict(movie) for movie in get_data(query).fetchall()]
    return result


def get_movie_by_genre(genre: str) -> list:
    """
    Get all movies by specified genre
    :param genre:   - genre for query
    :return:        - list of dicts of movies
    """
    query = f"""
            SELECT 
                `title`,
                `description`
            FROM `netflix`
            WHERE `type` = 'Movie' AND `listed_in` LIKE '%{genre}%'
            ORDER BY `release_year` DESC
            LIMIT 10
    """
    result = [dict(movie) for movie in get_data(query).fetchall()]
    return result


def get_most_played_with(first_actor: str, second_actor: str) -> list:
    """
    Get movies with actors played with mentioned two actors
    :param first_actor:     - first actor for query
    :param second_actor:    - second actor for query
    :return:                - movies with actors played with
    """
    # TODO: try to get_most_played_with by SQL request
    query = f"""
            SELECT 
                `cast`
            FROM `netflix`
            WHERE `cast` LIKE '%{first_actor}%' 
                AND `cast` LIKE '%{second_actor}%'
    """
    result = [dict(movie) for movie in get_data(query).fetchall()]
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
    query = f"""
            SELECT 
                `title`,
                `description`
            FROM `netflix`
            WHERE `type` LIKE '{video_type}'
                AND  `release_year` = '{release_year}'
                AND `listed_in` LIKE '%{listed_in}%' 
            """

    # TODO: find out how to trim (s.strip()) description in SQL request

    result = [
        {
            'title': dict(movie)['title'],
            'description': dict(movie)['description'].strip()
        }
        for movie in get_data(query).fetchall()
    ]

    return result
