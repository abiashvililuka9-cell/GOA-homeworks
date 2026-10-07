def sum_numbers(*args):
    return sum(args)



def largest_number(*args):
    return max(args)



def count_even(*args):
    return sum(1 for num in args if num % 2 == 0)



def average(*args):
    if not args:
        return 0
    return sum(args) / len(args)



def display_user_info(name, age, *args):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Other arguments: {args}")



def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")



def print_values(**kwargs):
    for value in kwargs.values():
        print(value)


def count_keys(**kwargs):
    return len(kwargs)




def combine_all(first_name, last_name, *args, **kwargs):
    print(f"Regular 1: {first_name}") 
    print(f"Regular 2: {last_name}")   
    print(f"Args: {args}")             
    print(f"Kwargs: {kwargs}") 

combine_all("Luka", "Abiashvili", 18, "Developer", city="Tbilisi", status="active")



def sum_numbers_kw(**kwargs):
    return sum(val for val in kwargs.values() if isinstance(val, (int, float)) and not isinstance(val, bool))



def execution_status_decorator(func):
    def wrapper(*args, **kwargs):
        print("Starting...")
        result = func(*args, **kwargs)
        print("Finished!")
        return result
    return wrapper



def welcome_decorator(func):
    def wrapper(*args, **kwargs):
        print("Welcome!")
        return func(*args, **kwargs)
    return wrapper


def border_decorator(func):
    def wrapper(*args, **kwargs):
        print("--------------------")
        result = func(*args, **kwargs)
        print("--------------------")
        return result
    return wrapper