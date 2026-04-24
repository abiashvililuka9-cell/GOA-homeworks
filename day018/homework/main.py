def average(numbers):
    return sum(numbers) / len(numbers)




def count_even(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count



def count_odd(numbers):
    count = 0
    for num in numbers:
        if num % 2 != 0:
            count += 1
    return count




def sum(a, b, c):
    return a + b + c




def substract(a, b):
    return a - b



def multiply(a, b):
    return a * b



def check_age(age):
    if age >= 18:
        print("Access Granted")
    else:
        print("Access Denied")




def odd_or_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"




def student_grade(score):
    if 90 <= score <= 100:
        print("A")
    elif 70 <= score <= 89:
        print("B")
    elif 50 <= score <= 69:
        print("C")
    elif 0 <= score <= 49:
        print("F")
    else:
        print("no score idk")




def user_info(first_name, last_name, age):
    return f"user name is {first_name}, surname {last_name} and age {age}."

