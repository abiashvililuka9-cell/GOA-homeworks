# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def introduce(self):
#         print(f"Hello, my name is {self.name} and I am {self.age} years old")


# p1 = Person("luka", 25)
# p1.introduce()









# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def perimeter(self):
#         return 2 * (self.width + self.height)


# rect = Rectangle(5, 10)
# print(f"area: {rect.area()}")
# print(f"perimeter: {rect.perimeter()}")


















# class Product:
#     def __init__(self, price, quantity):
#         self.price = price
#         self.quantity = quantity

#     def total_value(self):
#         return self.price * self.quantity

# products = [
#     Product(2500, 2),
#     Product(1500, 5),
#     Product(150, 10),
#     Product(50, 15)
# ]

# most_expensive = max(products, key=lambda p: p.price)
# cheapest = min(products, key=lambda p: p.price)

# print(f"dzviri: ({most_expensive.price} lari)")
# print(f"iapi: ({cheapest.price} lari)")
















class Dog:
    def __init__(self, breed, age, color):
        self.breed = breed
        self.age = age
        self.color = color

    def make_sound(self):
        print("Woof! Woof!")

    def bark(self):
        print(f"{self.age} years old {self.breed} is barking")


dog1 = Dog("German Shepherd", 3, "Black")
dog2 = Dog("Poodle", 2, "White")


print("Dog 1")
dog1.make_sound()
dog1.bark()


print("Dog 2")
dog2.make_sound()
dog2.bark()