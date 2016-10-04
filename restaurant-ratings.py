import random

def list_restaurant_ratings(file_name):
    with open(file_name) as restaurant_data:
        restaurants = {}

        for restaurant in restaurant_data:
            name, rating = restaurant.strip().split(':')
            restaurants[name] = rating


    while True:

        print "\nPlease choose an option. "
        print "1) See all restaurant ratings"
        print "2) Add a new restaurant"
        print "3) Update random restaurant"
        print "4) Update specific restaurant"
        print "5) Quit\n"

        choice = raw_input('Enter option: ')

        if choice == '5':
            break

        elif choice == '4':
            input_name = raw_input('Enter restaurant name: ')

            if input_name in restaurants:
                print 'The current rating is %s.' % (restaurants[input_name])
                restaurants[input_name] = raw_input('Enter new rating: ')

            else:
                print 'Restaurant not in file yet.'

        elif choice == '3':
            random_rest = random.choice(restaurants.keys())
            random_rating = raw_input('Enter new rating for %s: ' % (random_rest))
            restaurants[random_rest] = random_rating

        elif choice == '2':
            new_name = raw_input('Please enter restaurant name: ')
            new_rating = raw_input('Please rate the restaurant: ')

            restaurants[new_name] = new_rating

        elif choice == '1':
            for name, rating in sorted(restaurants.items()):
                print "%s is rated at %s" % (name, rating)

        else:
            print "Invalid input. Please choose again."

list_restaurant_ratings('scores.txt')

