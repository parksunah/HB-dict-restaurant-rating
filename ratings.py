


def restaurant_rating(filename):
    """Restaurant rating lister."""

    filename = open(filename)
    restaurant_rating = {}
    restaurant_name = input("Please enter a restaurant name. ").title()
    restaurant_score = int(input("Please enter the restaurant's score. "))

    for line in filename:
        line = line.rstrip()
        line = line.split(":")
        restaurant_rating[line[0]] = line[1]

    # add user input to the dictionary
    restaurant_rating[restaurant_name] = restaurant_score

    # returns a list of tuples that are the key, value pairs.
    # automatically sorts based on the first item of each tuple
    sorted_restaurants = sorted(restaurant_rating.items())  

    for name, rating in sorted_restaurants:
        print('{} is rated at {}'.format(name, rating))


restaurant_rating("scores.txt")
# put your code here

