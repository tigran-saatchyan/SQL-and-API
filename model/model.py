import sqlite3


def get_data(query):
    with sqlite3.connect('data/netflix.db') as con:
        con.row_factory = sqlite3.Row
        result = con.execute(query)
        return result


def get_movie_by_title(title):
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


def get_movies_in_year_range(from_year, to_year):
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


def get_data_by_rating_group(rating_list):

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


def get_movie_by_genre(genre):
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


def get_most_played_with(first_actor, second_actor):
    query = f"""
            SELECT 
                `cast`,
            FROM `netflix`
            WHERE `cast` LIKE '%{first_actor}%' 
                AND `cast` LIKE '%{second_actor}%'
    """
    result = [dict(movie) for movie in get_data(query).fetchall()]
    return result


def get_by_type_genre_and_year(video_type, listed_in, release_year):
    query = f"""
            SELECT 
                `title`,
                `description`
            FROM `netflix`
            WHERE `type` = '{video_type}'
                AND  `release_year` = '{release_year}'
                AND `listed_in` LIKE '%{listed_in}%' 
            """

    result = [
        {
            'title': dict(movie)['title'],
            'description': dict(movie)['description'].strip()
        }
        for movie in get_data(query).fetchall()
    ]

    return result
