

def list_restaurant_ratings(file_name):
    with open(file_name) as restaurant_data:
        restaurants = {}
        for restaurant in restaurant_data:
            name, rating = restaurant.strip().split(':')
            restaurants[name] = rating

    
        for name, rating in sorted(restaurants.items()):
            print name, rating

list_restaurant_ratings('scores.txt')
