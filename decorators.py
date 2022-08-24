# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper_function(*args):
        print(f"You called the function {function.__name__}{args}")
        function()
        print(f"It returned: {function(*args)}")
    return wrapper_function


# Use the decorator 👇
@logging_decorator
def function_a(*args):
    x = 0
    for i in args:
        x = x + i
    return x

function_a(5, 2, 6)