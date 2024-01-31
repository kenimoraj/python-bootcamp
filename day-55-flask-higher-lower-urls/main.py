from flask import Flask
import random

app = Flask(__name__)

secret = random.randint(0, 9)

@app.route("/")
def main_screen():
    return ("<h1>Guess a number from 0 to 9!</h1>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>")

@app.route("/<int:number>")
def guess_result(number):
    if number < secret:
        result = ("<h1>Too low!</h1>"
                  "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>")
    elif number > secret:
        result = ("<h1>Too high!</h1>"
                  "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>")
    else:
        result = ("<h1>Correct!</h1>"
         "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>")
    return result


if __name__ == "__main__":
    app.run(debug=True)

