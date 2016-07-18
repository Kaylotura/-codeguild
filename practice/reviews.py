"""Reads a database of businesses, users, and reviews, and can return grouping information."""


import json
import statistics


def open_file_to_dictionary(file):
    with open(file) as source:
        lines = source.readlines()
    return [json.loads(line) for line in lines]


def load_users():
    return open_file_to_dictionary('Reviews/users.txt')


def load_reviews():
    return open_file_to_dictionary('Reviews/reviews.txt')


def load_businesses():
    return open_file_to_dictionary('Reviews/business.txt')


def get_reviews_for_business(name, reviews):
    busines_reviews = [review for review in reviews if review['business_name'] == name]
    print(busines_reviews)
    return busines_reviews


def get_mean(reviews):
    ratings = [review['rating'] for review in reviews]
    mean_rating = statistics.mean(ratings)
    print(mean_rating)
    return mean_rating

def get_reviews_for_user(name, reviews):
    user_reviews = [review for review in reviews if review['user_name'] == name]
    print(user_reviews)
    return user_reviews


def main():
    business_name = 'Voodoo Donuts'
    user_name = 'Abby'
    city = 'Portland'
    users = load_users()
    reviews = load_reviews()
    businesses = load_businesses()
    reviews_for_business = get_reviews_for_business(business_name, reviews)
    mean_for_biz = get_mean(reviews_for_business)
    reviews_for_user = get_reviews_for_user(user_name, reviews)
    mean_rating_for_hometown = get_mean_rating_for_hometown()
# if city in users mean rating



if __name__ == '__main__':
    main()
