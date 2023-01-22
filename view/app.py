from flask import Flask, jsonify

from controller import controller

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False


@app.route('/movie/<title>')
def movie_by_title(title):
    return jsonify(controller.get_movie_by_title(title))


@app.route('/movie/<int:from_year>/to/<int:to_year>')
def movie_in_range(from_year, to_year):
    return jsonify(controller.get_movies_in_year_range(from_year, to_year))


@app.route('/rating/<rating_group>')
def movie_and_tv_show_by_rating_group(rating_group):
    return jsonify(controller.get_data_by_rating_group(rating_group))


@app.route('/genre/<genre>')
def movie_by_genre(genre):
    return jsonify(controller.get_movie_by_genre(genre))


@app.route('/movie/cast/<first_actor>/<second_actor>')
def most_played_with(first_actor: str, second_actor: str):
    return jsonify(controller.get_most_played_with(first_actor, second_actor))


@app.route('/search/<video_type>/<listed_in>/<int:release_year>')
def by_type_genre_and_year(video_type, listed_in, release_year):
    return jsonify(
        controller.get_by_type_genre_and_year(
            video_type,
            listed_in,
            release_year
        )
    )


if __name__ == "__main__":
    app.run(debug=True)
