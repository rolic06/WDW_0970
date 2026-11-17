cities = ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai", "Delhi"]


unique_citiees = set(cities)
print("city no. 2:", cities[1])
print("Total entries:", len(cities))
print("Unique cities:", unique_citiees)
print("Number of unique cities:", len(unique_citiees))
print("num values", len(cities)/5 + len(unique_citiees)*0.5)

# Notice the None value representing a blank cell
ratings = [4.5, 5.0, None, 3.8, None, 4.2]
valid_ratings = []

for r in ratings:
    if r is not None:
        valid_ratings.append(r)

average_rating = sum(valid_ratings) / len(valid_ratings)
print("Valid ratings:", valid_ratings)
print("Average rating:", round(average_rating, 2))

