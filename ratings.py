"""Restaurant rating lister."""
def restaurant_rating(filename):
    filename = open(filename)
    restaurant_rating = {}
    restaurant_name = input("Please enter a restaurant name. ").capitalize()
    restaurant_score = int(input("Please enter the restaurant's score. "))

    for line in filename:
        line = line.rstrip()
        line = line.split(":")
        restaurant_rating[line[0]] = line[1]

    restaurant_rating[restaurant_name] = restaurant_score

    sorted_restaurant = sorted(restaurant_rating) # sorted list of keys
    restaurant_rating2 = {}

    for key in sorted_restaurant:
        restaurant_rating2[key] = restaurant_rating[key]

    for name, rating in restaurant_rating2.items():
        print('{} is rated at {}'.format(name, rating))


restaurant_rating("scores.txt")
# put your code here

