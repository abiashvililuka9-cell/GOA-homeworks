def pipqebi(func):
    def rame(*args, **kwargs):
        result = func(*args, **kwargs)
        return f'***{result}'
    return rame

@pipqebi
def greet():
    return 'gaumarjos'



def add_five(func):
    def raime(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + 5
    return raime


@add_five
def int1():
    return 5

@add_five
def int2():
    return 10

@add_five
def int3():
    return 15

@add_five
def int4():
    return 20