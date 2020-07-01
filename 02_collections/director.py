import csv

# open the csv file
with open('movie_data.csv', 'r') as movie_data:
    # read the file into a dictionary
    csv_reader1 = csv.DictReader(movie_data)

    # Create dictionaries to store the list of directors and movies
    directors = {}
    movies = {}

    for line in csv_reader1:
        # Populate the dictionary of directors with and the number of films
        if line['title_year'] and int(line['title_year']) > 1980:
            if line['director_name'] not in directors:
                directors[line['director_name']] = 0
            directors[line['director_name']] += 1

        # Populate the dictionary of movies by director
        if line['title_year'] and int(line['title_year']) > 1980:
            if line['director_name'] not in movies:
                movies[line['director_name']] = [[line['movie_title'], line['title_year']]]
            else:
                movies[line['director_name']].append([line['movie_title'], line['title_year']])

    # list of top 20 directors in descending order
    sorted_directors = sorted(directors.items(),
                              key=lambda x: x[1], reverse=True)

    # initiate a variable to track the rank of the directors
    director_rank = 1

    # print out the movies and release years for each of the top 20 directors
    for director in sorted_directors[:20]:
        print(f'#{director_rank} {director[0]}')
        director_rank += 1
        for movie in movies:
            if movie == director[0]:
                for film in movies[director[0]]:
                    print(f'\t "{film[0].rstrip()}", {film[1]}')
        print("-" * 60)

# ['color', 'director_name', 'num_critic_for_reviews', 'duration', 'director_facebook_likes', 'actor_3_facebook_likes', 'actor_2_name', 'actor_1_facebook_likes', 'gross', 'genres', 'actor_1_name', 'movie_title', 'num_voted_users', 'cast_total_facebook_likes', 'actor_3_name', 'facenumber_in_poster', 'plot_keywords', 'movie_imdb_link', 'num_user_for_reviews', 'language', 'country', 'content_rating', 'budget', 'title_year', 'actor_2_facebook_likes', 'imdb_score', 'aspect_ratio', 'movie_facebook_likes']
