import random
from flask import Flask, request, redirect, url_for, render_template
from flask_restful import reqparse

app = Flask(__name__)
wsgi_app = app.wsgi_app
guessedNum_post_args = reqparse.RequestParser()
guessedNum_post_args.add_argument("guessedNum", type=int, help="Thats not a number", required=True)
global rnum
def generate():
    global rnum
    rnum = random.randrange(1,101)
    return rnum
# print(x)

rnum = generate()

@app.route("/guessgame", methods=["POST", "GET"], )
def guess():
    global rnum, counter
    message = ""
    if request.method == "POST":
        guessedNum = int(request.form["nb"])
        if guessedNum == rnum:
            return redirect(url_for('gameover'))
        elif guessedNum < rnum:
            message = "Your guess was too low"
        elif guessedNum > rnum:
            message = "Your guess was too high"
    return render_template("guessgame.html", message = message)

@app.route("/gameover", methods=["POST", "GET"])
def gameover():
    if request.method == "GET":
        message = "You Win... The secret number was " + str(rnum)
        return render_template("gameover.html", message = message)
    elif request.method == "POST":
        if request.form['btnPlayAgain'] == 'Play Again':
            generate()
            return redirect(url_for('guess'))
    return render_template("gameover.html")


if __name__ == "__main__":
    app.run(debug=True)
