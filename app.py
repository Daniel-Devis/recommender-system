from flask import Flask, render_template, request, jsonify
from recommendation import MovieRecommender

app = Flask(__name__)
recommender = MovieRecommender()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    movie_title = data['movieTitle']
    genre = data.get('genre', '')

    matched_id, matched_title = recommender.movie_finder(movie_title)

    if matched_id is None:
        # Return a simple message indicating no match was found
        return jsonify({'matched_title': None, 'message': 'Oops! No similar movies were found for the given title. Try another one!'}), 200

    similar_movies_ids = recommender.find_similar_movies(matched_id, desired_genre=genre)

    result_titles = []
    for movie_id in similar_movies_ids:
        movie_data = recommender.movies[recommender.movies['movieId'] == movie_id]
        title = movie_data['title'].iloc[0] if not movie_data['title'].empty else 'Unknown Title'
        imdb_id = movie_data['imdbId'].iloc[0] if not movie_data['imdbId'].empty else 'N/A'
        result_titles.append({'title': title, 'imdbId': imdb_id})

    return jsonify({'matched_title': matched_title, 'recommendations': result_titles, 'genre': genre})


if __name__ == '__main__':
    app.run(debug=True)