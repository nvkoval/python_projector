# 1. Create a decorator that will check types.
# It should take a function with arguments and validate inputs with annotations.
'''Example:

@check_types
def add(a: int, b: int) -> int:
    return a + b

add(1, 2)
> 3

add(1, "2")
> TypeError: Argument b must be int, not str
'''


def check_types(func):
    def wrapper(*args):
        dict_args = {key: type(var) for key, var in zip(func.__annotations__.keys(), args)}
        dict_func_anot = func.__annotations__
        err = 0
        for k in dict_args.keys():
            if dict_args[k] != dict_func_anot[k]:
                print(f"TypeError: Argument {k} must be {dict_func_anot[k]}, not {dict_args[k]}")
                err += 1
        if err == 0:
            print(func(*args))
    return wrapper


@check_types
def add(a: int, b: int) -> int:
    return a + b


add(1, "2")
print("*"*10)
add(1, 2)
print("*"*10)
add("1", "2")

# 2. Write a decorator that will calculate the execution time of a function.
'''Example:

    @calculate_execution_time
    def add(a: int, b: int) -> int:
        return a + b

    add(1, 2)
    > 3
    > Execution time: 0.0005 seconds
    '''

from time import time


def calculate_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        print(func(*args, **kwargs))
        end_time = time()
        print(f"Execution time: {round(end_time - start_time, 6)} seconds")
    return wrapper


@calculate_execution_time
def add(a: int, b: int) -> int:
    return a + b


add(1, 2)
