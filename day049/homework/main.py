celsius = [0, 25, 100, -10, 37]
kelvin = list(map(lambda c: c + 273, celsius))







numbers = [2, 4, 6, 8, 10]
squared = list(map(lambda x: x ** 2, numbers))









usernames = [input() for _ in range(5)]
greet_users = list(map(lambda name: f"Welcome {name}", usernames))









cars = {
    "BMW": 1998,
    "Mercedes": 2005,
    "Audi": 1995,
    "Toyota": 2012,
    "Honda": 1999
}
old_years = list(filter(lambda car: cars[car] < 2000, cars))








usernames = [input() for _ in range(5)]
filtered_users = list(filter(lambda name: len(name) > 5, usernames))