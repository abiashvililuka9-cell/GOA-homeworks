students = {
    "Nika": 85,
    "Mariam": 45,
    "Giorgi": 70
}

students["Ana"] = 90

students["Mariam"] = 60


passed_students = [name for name, grade in students.items() if grade > 50]

print(students)
print(passed_students)











numbers = [1, 2, 3, 4, 5, 6]

squares = [num ** 2 for num in numbers]

even_squares = [num for num in squares if num % 2 == 0]

print(squares)
print(even_squares)








words = ["Python", "AI", "Development", "Code", "Learning", "Data"]

long_words = [word for word in words if len(word) > 4]

print(long_words)








words = ["Python", "AI", "Development", "Code", "Learning", "Data"]

long_words = [word for word in words if len(word) > 4]

print(long_words)








products = {
    "Milk": 2.5,
    "Bread": 1.5,
    "Cheese": 4.2,
    "Juice": 3.5,
    "Eggs": 2.8
}

expensive_products = [product for product, price in products.items() if price > 3]

print(expensive_products)