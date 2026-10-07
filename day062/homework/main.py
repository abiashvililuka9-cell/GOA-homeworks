class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department



class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


class Admin(User):
    def __init__(self, username, email, role):
        super().__init__(username, email)
        self.role = role



class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class EBook(Book):
    def __init__(self, title, author, file_size, format_type):
        super().__init__(title, author)
        self.file_size = file_size
        self.format_type = format_type



class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        print(f"{self.name}'s salary is {self.salary}")


class Manager(Employee):
    def bonus_salary(self):
        self.salary *= 1.20
        return self.salary



class Vehicle:
    def __init__(self, brand, year, color, horse_power):
        self.brand = brand
        self.year = year
        self.color = color
        self.horse_power = horse_power

    def drive(self):
        print(f"{self.color} {self.brand} is going")

    def stop(self):
        print(f"{self.color} {self.brand} is stopping")


class Car(Vehicle):
    def open_trunk(self):
        print(f"Opening the trunk of {self.brand}")


class Motorcycle(Vehicle):
    def pop_wheelie(self):
        print(f"{self.brand} is popping a wheelie!")


class Bike(Vehicle):
    def ring_bell(self):
        print(f"Ring ring! {self.brand} bell sounds.")