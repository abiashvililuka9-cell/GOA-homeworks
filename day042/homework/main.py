# პროგრამირებაში ორი ტიპის ერორია: 

# 1)მცირე შეცდომა კოდში რომელიც არ იწვევს სისტემის შეფერხებას:
# logical error

# 2)შეცდომა რომელიც აფერხებს კოდს:
# ZeroDivisionError
# KeyError
# ValueError
# TypeError
# IndexError
# NameError






# ZeroDivisionError წარმოიქმნება მაშინ, როდესაც რიცხვის გაყოფას ვცდილობთ 0 ზე.






# try:
#     num1 = int(input("Enter your number: "))
#     num2 = int(input("Enter your number 2: "))

#     print(num1 / num2)

# except ZeroDivisionError:
#     print("Can't divide a number by 0.")








# user = {
#     "name": "Luka",
#     "age": 16,
#     "surname": "abiashvili"
# }

# try:
#     print(user["email"])

# except KeyError:
#     print("This key does not exist.")










# finally:
# სრულდება ყოველთვის, მიუხედავად იმისა მოხდა თუ არა შეცდომა.

# else:
# სრულდება მხოლოდ მაშინ, თუ try ბლოკში შეცდომა არ მოხდა.

# raise:
# გამოიყენება შეცდომის (Exception-ის) ხელოვნურად გამოსაწვევად.









# def divide(a, b):
#     try:
#         return a / b

#     except ZeroDivisionError:
#         return "Can't divide by zero."


# print(divide(10, 2))
# print(divide(10, 0))










# try:
#     print("Trying...")

# except:
#     print("Error encountered")

# finally:
#     print("Code cleanup is done")










# def check_password(password):
#     try:
#         if len(password) < 8:
#             raise ValueError("Password too short")

#         if " " in password:
#             raise ValueError("Password cannot contain spaces")

#         return "Password accepted"

#     except:
#         return 'error'


# print(check_password("abc"))
# print(check_password("my pass123"))
# print(check_password("mypassword123"))