"""Reads a database of businesses, users, and reviews, and can return grouping information."""


import json
import statistics


def open_file_to_dictionary(file):
    """Opens file, and loads JSON to a lines of text."""
    with open(file) as source:
        lines = source.readlines()
    return [json.loads(line) for line in lines]


def load_users():
    """Loads users data from text file"""
    return open_file_to_dictionary('Reviews/users.txt')


def load_reviews():
    """Loads reviews data from text file"""
    return open_file_to_dictionary('Reviews/reviews.txt')


def load_businesses():
    """Loads business data from text file"""
    return open_file_to_dictionary('Reviews/business.txt')


def get_reviews_for_business(name, reviews):
    """Gets all reviews for a given business in a list.

    >>> get_reviews_for_business('Lori', [{'business_name':'Lori'}{business_name':'Jake}])
    [{'business_name':'Lori'}]
    """
    busines_reviews = [review for review in reviews if review['business_name'] == name]
    return busines_reviews


def get_mean(reviews):
    """Finds and returns mean for ratings in reviews list.

    >>> get_mean([{'business_name':'Lori', 'rating': 5}, {business_name':'Jake', 'rating':3}])
    4
    """
    ratings = [review['rating'] for review in reviews]
    mean_rating = statistics.mean(ratings)
    return mean_rating


def get_reviews_for_user(name, reviews):
    """Finds and returns all reviews for a given user

    >>> get_reviews_for_user('Lori', [{'user_name':'Lori', 'rating', 5}, {'user_name':'Jake', 'rating', 3}])
    {'user_name':'Lori', 'rating', 5}
    """
    user_reviews = [review for review in reviews if review['user_name'] == name]
    return user_reviews


def get_all_users_from_single_city(users, city):
    """Finds all users from a given city

    >>> get_all_users_from_single_city([{"user_name": "Abby", "hometown": "Portland"}, {"user_name": "Helen", "hometown": "Bugs"}],[Portland])
    'Abby'
    """
    users_from_city = [user['user_name'] for user in users if user['hometown'] == city]
    return users_from_city


def get_all_ratings_from_user_names(users_from_city, reviews):
    """Creates a list of ratings from a given user

    >>> get_all_ratings_from_user_names('Carmen',[{"user_name": "Carmen", "business_name": "Dicks Burgers", "rating": 2, "text": "Gross meat."}]
    [2]
    """
    city_ratings = [review['rating'] for review in reviews if review['user_name'] in users_from_city]
    return city_ratings


def get_mean_rating_for_hometown(users, city, reviews):
    """Retuns the mean rating for a given city

    >>>get_mean_rating_for_hometown([{"user_name": "Abby", "hometown": "Portland"}, {"user_name": "Helen", "hometown": "Bugs"}]), 'Portland', reviews)
    3.5
    """
    users_from_city = get_all_users_from_single_city(users, city)
    city_ratings = get_all_ratings_from_user_names(users_from_city, reviews)
    mean_of_ratings_for_city = statistics.mean(city_ratings)
    return (mean_of_ratings_for_city)


def get_user_input_queery():
    print('Welcome to Yelplike!')
    print('1: See all reviews for a business')
    print('2: See average rating for a business')
    print('3: See all reviews from a user')
    print('4: See average ratings for a city')
    user_input = input('What would you like to see? ')
    return user_input

def cast_to_string(list):
    return [str(item) for item in list if type(item) == int]

def clean_up_dictionaries(list_of_dictionaries):
    final_list = []
    for dictionary in list_of_dictionaries:
        temp = []
        for value in (dictionary.values()):
            temp.append(str(value))
        final_list.append(' '.join(temp))
    for value in final_list:
        print(value)

def see_all_reviews_for_a_biz(reviews):
    business_name = input('What business would you like to see reviews for? ')
    dict_reviews_for_business = get_reviews_for_business(business_name, reviews)
    clean_texts = clean_up_dictionaries(dict_reviews_for_business)
    return clean_texts


def run_queery(user_queery, users, reviews, businesses):
    if user_queery == '1':
        all_reviews_for_a_biz = see_all_reviews_for_a_biz(reviews)
    elif user_queery == '2':
        business_name = input('What business would you like to see the average rating for? ')
        reviews_for_business = get_reviews_for_business(business_name, reviews)
        mean_for_biz = get_mean(reviews_for_business)
        print(mean_for_biz)
    elif user_queery == '3':
        user_name = input('What user would you like to see reviews for? ')
        reviews_for_user = get_reviews_for_user(user_name, reviews)
        clean_texts = clean_up_dictionaries(reviews_for_user)
    elif user_queery == '4':
        city = input('What city would you like to see average ratings for? ')
        mean_rating_for_hometown = get_mean_rating_for_hometown(users, city, reviews)
        print(mean_rating_for_hometown)


def main():
    users = load_users()
    reviews = load_reviews()
    businesses = load_businesses()
    users_queery = get_user_input_queery()
    queery = run_queery(users_queery, users, reviews, businesses)
if __name__ == '__main__':
    main()
