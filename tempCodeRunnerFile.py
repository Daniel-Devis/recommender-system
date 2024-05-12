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
    matched_id, matched_title = recommender.movie_finder(movie_title)
    similar_movies_ids = recommender.find_similar_movies(matched_id)

    result_titles = [recommender.movies[recommender.movies['movieId'] == movie_id]['title'].iloc[0] for movie_id in similar_movies_ids]
    
    # Send back both the matched title and the recommendations
    return jsonify({'matched_title': matched_title, 'recommendations': result_titles})

if __name__ == '__main__':
    app.run(debug=True)
