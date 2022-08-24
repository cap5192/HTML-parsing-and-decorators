from flask import Flask
app = Flask(__name__)

#Requirement
#Create decorater function to add HTML tags for underline, emphasis and bold

def make_bold(function):
    def wrapper_function():
        x = function()
        y = f"<strong>{x}</strong>"
        return y
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        x = function()
        y = f"<em>{x}</em>"
        return y
    return wrapper_function

def make_underlined(function):
    def wrapper_function():
        x = function()
        y = f"<u>{x}</u>"
        return y
    return wrapper_function

@app.route('/')
@make_bold
@make_emphasis
@make_underlined
def index():
    return 'Index Page'

# @app.route('/<username>')
# def hello(username):
#     return f"Hello, World, {username}"

if __name__ == '__main__':
    app.run(debug=True)