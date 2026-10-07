# 1) შექმენით Person კლასი (name, age).
# შემდეგ შექმენით Student კლასი, რომელიც ამატებს grade-ს და super()-ით ინიციალიზაციას აკეთებს.

# 2) შექმენით Shape კლასი area() მეთოდით რომელიც დააბრუნებს საწყისად 0-ს (return 0).
#შემდეგ შექმენით Rectangle კლასი (width, height), რომელიც super()-ს გამოიყენებს და მოახდენს area() მეთოდის override-ს.





class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade


student1 = Student('luka', 16, 10)
print(student1.name, student1.age, student1.grade)



class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def area(self):
        return self.width * self.height


rectangle1 = Rectangle(5, 4)
print(rectangle1.area())