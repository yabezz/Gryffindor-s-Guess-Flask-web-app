from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def guess_the_number():
    if request.method == "POST":
        num = int(request.form["num"])
        guess = int(request.form["guess"])
        if guess > num:
            message = "Your guess is higher!"
        elif guess < num:
            message = "Your guess is lower!"
        else:
            message = "You won!"
        return render_template("index.html", message=message, num=num)
    else:
        num = random.randint(1, 20)
        return render_template("index.html", num=num)

if __name__ == "__main__":
    app.run(debug=True)
