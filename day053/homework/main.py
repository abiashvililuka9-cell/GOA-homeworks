import time


def say_hello(func):
    def wrapper(*args, **kwargs):
        print("ფუნქცია იწყებს მუშაობას...")
        result = func(*args, **kwargs)
        print("ფუნქციამ დაასრულა მუშაობა!")
        return result
    return wrapper



def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"ფუნქციის შესრულების დრო: {execution_time:.6f} წამი")
        return result
    return wrapper



def start_finish_decorator(func):
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