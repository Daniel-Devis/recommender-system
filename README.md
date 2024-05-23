# Movie Recommender System

This project is a movie recommender system developed as part of the Applications of Artificial Intelligence, Machine Learning, and Data Science (CSC-40070) module at Keele University. The system leverages item-based collaborative filtering with genre filtering to provide relevant movie recommendations without requiring user personal information.

![Web App Overview](https://github.com/FredSabu/Movie_Recommender/assets/130511381/8fefcb2f-0cec-4662-9827-98add059f95c)  
*Figure 1: Overview of the web application.*

## Table of Contents

- [Introduction](#introduction)
- [Challenges](#challenges)
  - [Privacy](#privacy)
  - [Cold Start Problem](#cold-start-problem)
  - [Sparsity](#sparsity)
- [Approach](#approach)
- [Dataset](#dataset)
- [Feature Extraction](#feature-extraction)
- [Machine Learning](#machine-learning)
- [Web Application Design](#web-application-design)
- [Evaluation](#evaluation)
- [Conclusion and Future Work](#conclusion-and-future-work)
- [Contributors](#contributors)

## Introduction

Recommender systems have become a ubiquitous feature of modern digital platforms, significantly shaping how we interact with media and make purchasing decisions. This project explores the development and application of a movie recommender system, focusing on its underlying algorithms, design choices, and impact on user satisfaction.

## Challenges

### Privacy

Our system addresses privacy concerns by not requiring users to input any personal information. Users simply enter a movie title to receive recommendations, ensuring no personal data is collected or stored.

### Cold Start Problem

We mitigate the cold start problem by incorporating genre-based filtering alongside item-based collaborative filtering. This approach ensures relevant recommendations even without user data, leveraging similarities in genres and user ratings of similar movies.

### Sparsity

To tackle sparsity, our system employs K-Nearest Neighbors (KNN) with cosine similarity, effective even with sparse data. Preprocessing steps enhance the dataset, making it richer and more informative for the recommendation process.

![Number of Ratings Per User](https://github.com/FredSabu/Movie_Recommender/assets/130511381/a30a371c-333d-49f7-b9b5-09dbdba11798)  
*Figure 2: Visualisation showing the distribution of the number of ratings per user.*

![Number of Ratings Per Movie](https://github.com/FredSabu/Movie_Recommender/assets/130511381/6a8fe9c4-9bfa-4955-9073-dd1e3383722c)  
*Figure 3: Visualisation showing the distribution of the number of ratings per movie.*

## Approach

Our system uses item-based collaborative filtering with genre filtering to provide relevant movie recommendations. This approach excels in discovering new interests through user behavior patterns without requiring personal data.

## Dataset

We use the [MovieLens 25M dataset](https://grouplens.org/datasets/movielens/25m/), which includes user ratings, movie metadata, and tag applications. This comprehensive dataset is suitable for developing complex recommendation algorithms.

We have received permission to use the dataset for educational and academic research purposes (non-commercial use). 

## Feature Extraction

In our movie recommender system, we extract and utilise several key features from the MovieLens 25M dataset to facilitate the recommendation process. Below are the details of the features and how they are used:

- **Movie Titles**: The titles of the movies are used for matching user input and generating recommendations. Titles are cleaned and standardized to ensure consistency.
  
- **Release Year**: The release year is extracted from the movie titles. This feature helps in organizing and filtering movies, allowing for more precise recommendations based on user preferences for specific periods.

- **Genres**: Genres are split into individual elements to facilitate genre-based filtering. This allows the recommender system to cater to user preferences for specific genres, improving the relevance of the recommendations.

- **User Ratings**: User ratings are the backbone of our collaborative filtering approach. These ratings are used to create the user-item interaction matrix, which forms the basis of the KNN algorithm to find similar movies.

- **IMDb IDs**: Unique identifiers for movies in the IMDb database are used to enrich the dataset with additional metadata. This enhances the recommendation process by providing more detailed information about each movie.

- **Movie IDs**: Unique identifiers for movies in the MovieLens dataset are used to map movies in the user-item interaction matrix and to link various pieces of information together during data processing and analysis.

![Distribution of Movie Ratings](https://github.com/FredSabu/Movie_Recommender/assets/130511381/7387a02e-1a56-4ac0-b668-0957e7c9fa5d)  
*Figure 4: Visualisation showing the distribution of movie ratings.*

## Machine Learning

Our system uses K-Nearest Neighbors (KNN) with cosine similarity to find the most similar movies based on user ratings. This approach ensures personalized recommendations based on individual user rating patterns.

![Example of Movie Recommendations](https://github.com/FredSabu/Movie_Recommender/assets/130511381/a1e52499-4b8d-43ff-a086-1ed6540c2a56)  
*Figure 5: Example of movie recommendations generated by the system.*

![Example of Movie Recommendations with Genre Filtering](https://github.com/FredSabu/Movie_Recommender/assets/130511381/1374e83d-b568-40f9-a2f0-11a1f911dc5b)  
*Figure 6: Example of movie recommendations with genre filtering applied.*

## Web Application Design

### User-Friendly Interface and Aesthetics

The application features a cohesive design with a consistent color scheme, modern fonts, and a responsive layout ensuring accessibility across devices.

### Performance, Responsiveness, and User Interaction

The application optimizes user interaction with asynchronous operations for real-time feedback and a smooth user experience.

![Web App Screenshot 2](https://github.com/FredSabu/Movie_Recommender/assets/130511381/7df55b42-42cf-4cd7-9202-883605e4a34b)  
*Figure 7: Loading indicator while fetching movie recommendations for "Interstellar."*

### Integration with Backend Systems

We ensured seamless integration between the frontend UI and backend recommendation system, handling data communication, real-time updates, and error management effectively.

## Evaluation

The system was evaluated using precision, recall, and accuracy metrics, achieving the following results:

- **Precision**: 0.84
- **Recall**: 0.38
- **Accuracy**: 0.42

These metrics indicate that the system effectively matches users' preferences, though there is room for improvement in recall and accuracy.

## Conclusion and Future Work

Our recommender system successfully avoids personal data collection while providing relevant movie recommendations. Future enhancements include incorporating feature extraction, autofill functionality, and a live dataset for more up-to-date movie suggestions.

## Contributors

This project was a collaborative effort by:

- **Fred Sabu (18005389)**: Chief Architect and Developer, led front-end and recommender system development.
- **Daniel Devis (19020322)**: Development Support Specialist, assisted in development, testing, and feedback.
- **Mathi Kumaran (20021974)**: Data Processing Lead, handled preprocessing, feedback, testing, and assisted in development.
- **Reynold Kwok (23003788)**: Evaluation Lead, conducted evaluation, feedback, testing, and assisted in development.


