import os

def debugger(func):
    def wrapper(*args, **kwargs):
        # print the fucntion name and arguments
        print(f"Calling {func.__name__} with args: {args} kwargs: {kwargs}")
        # call the function
        result = func(*args, **kwargs)
        # print the results
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

if __name__ == '__main__':
    @debugger
    def add_numbers(x, y):
        return x + y
    add_numbers(7, y=5,)  