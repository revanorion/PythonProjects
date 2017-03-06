import csv, sys


def open_csv(filename, keysid, valuesid, skip=""):
    """
    Opens any CSV based on filename.
    :param filename:  CSV File name
    :param keysid: tuple of key value location
    :param valuesid: tuple of values location
    :param skip: string to skip. used for heading
    :return: dictionary of key values
    """
    with open(filename, 'rt', encoding="utf8") as f:
        reader = csv.reader(f)
        try:
            values = []
            keys = []
            for row in reader:
                if skip not in row:
                    key = [x for i, x in enumerate(row) if i in keysid]
                    value = [x for i, x in enumerate(row) if i in valuesid]
                    keys.append(tuple(key))
                    values.append(tuple(value))
            return dict(zip(keys, values))
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))


def get_top_rated_directors(top_rated, top_casts):
    """
    Gets all directors who directed top rated movies
    :param top_rated: dictionary of top rated movies
    :param top_casts: dictionary of top casts
    :return: sorted list of top rated movie directors
    """
    top_directors = {}
    for rated in top_rated:
        director = top_casts[rated][0]
        if director in top_directors:
            top_directors[director] += 1
        else:
            top_directors.update({director: 1})
    top = sorted(top_directors.items(), key=lambda x: x[1], reverse=True)
    return top


def get_top_grossing_directors(top_grossing, top_casts):
    """
    Gets all directors who directed top grossing movies
    :param top_grossing: dictionary of top grossing movies
    :param top_casts: dictionary of top casts
    :return: sorted list of top grossing movie directors
    """
    top_directors = {}
    for grossing in top_grossing:
        director = top_casts[grossing][0]
        if director in top_directors:
            top_directors[director] += 1
        else:
            top_directors.update({director: 1})
    top = sorted(top_directors.items(), key=lambda x: x[1], reverse=True)
    return top


def get_top_rated_actors(top_rated, top_casts):
    """
    Gets all actors with the most movie credits from the top rated list.
    :param top_rated: dictionary of top rated movies
    :param top_casts: dictionary of top rated casts
    :return: sorted list of actors with number of roles they stared in for a top rated movie
    """
    top_actors = {}
    for rated in top_rated:
        actors = top_casts[rated]
        for actor_index in range(1, 5):
            if actors[actor_index] in top_actors:
                top_actors[actors[actor_index]] += 1
            else:
                top_actors.update({actors[actor_index]: 1})
    top = sorted(top_actors.items(), key=lambda x: x[1], reverse=True)
    return top


def get_top_grossing_actors(top_grossing, top_casts):
    """
    Gets all actors who brought in the most box office money, based on the top grossing movie list
    :param top_grossing: dictionary of top grossing movies
    :param top_casts: dictionary of top casts
    :return: sorted list of of actors and their gross earnings
    """
    top_actors = {}
    for grossing in top_grossing:
        actors = top_casts[grossing]
        gross = int(top_grossing[grossing][1])

        update_actor(top_actors, actors[1], gross, 16)
        update_actor(top_actors, actors[2], gross, 8)
        update_actor(top_actors, actors[3], gross, 4)
        update_actor(top_actors, actors[4], gross, 2)
        update_actor(top_actors, actors[5], gross)
    top = sorted(top_actors.items(), key=lambda x: x[1], reverse=True)
    return top


def update_actor(top_actors, actor, gross, amount=1):
    """
    Updates top actors with earning
    :param top_actors: list of top actors
    :param actor: actor's name
    :param gross: gross amount of movie
    :param amount: amount of earning actor should be paid
    :return: None
    """
    money = amount * (gross / 31)
    if actor in top_actors:
        top_actors[actor] += money
    else:
        top_actors.update({actor: money})


def get_movies_ranking(top_rated, top_grossing):
    """
    Gets all rankings of movies based on a combined rating/grossing score
    :param top_rated: dictionary of top rated movies
    :param top_grossing: dictionary of top grossing movies
    :return: sorted list of movies ranked on rating and grossing score
    """
    movies = [(x, (top_rated[x][0], top_grossing[x][0])) for x in top_grossing if x in top_rated]
    movie_score = []
    for movie in movies:
        movie_score.append((movie[0], 500 - float(movie[1][0]) - float(movie[1][1])))
    ranking = sorted(movie_score, key=lambda x: x[1], reverse=True)
    return ranking


# These lines will have all the data from the CSV stored as a dictionary
filename = 'imdb-top-casts.csv'
top_casts = open_csv(filename, (0, 1), (2, 3, 4, 5, 6, 7))
filename = 'imdb-top-grossing.csv'
top_grossing = open_csv(filename, (1, 2), (0, 3), "Rank")
filename = 'imdb-top-rated.csv'
top_rated = open_csv(filename, (1, 2), (0, 3), "Rank")

# these lines will have the computed return values of the executed functions
top_rated_directors = get_top_rated_directors(top_rated, top_casts)
top_grossing_directors = get_top_grossing_directors(top_grossing, top_casts)
top_actors = get_top_rated_actors(top_rated, top_casts)
movie_rankings = get_movies_ranking(top_rated, top_grossing)
top_grossing_actors = get_top_grossing_actors(top_grossing, top_casts)

# the folling lines will print the result of the executed functions
print('Director'.ljust(20) + 'Movies in top rated list')
print('-' * 50)
for x in range(5):
    print(top_rated_directors[x][0].ljust(20), str(top_rated_directors[x][1]).rjust(10))

print('\n\nDirector'.ljust(20) + 'Movies in top grossing list')
print('-' * 50)
for x in range(5):
    print(top_grossing_directors[x][0].ljust(20), str(top_grossing_directors[x][1]).rjust(10))

print('\n\nActors with the most movie credits from the top rated list')
print('-' * 50)
for x in range(5):
    print(top_actors[x][0].ljust(20))

print('\n\nMovies'.ljust(60) + 'Year'.ljust(10))
print('-' * 40 + 'based on a combined rating/grossing score' + '-' * 40)
for x in range(5):
    print(movie_rankings[x][0][0].ljust(50), str(movie_rankings[x][0][1]).rjust(10))

print('\n\nActors who brought in the most box office money')
print('-' * 50)
for x in range(5):
    print(top_grossing_actors[x][0].ljust(20))
