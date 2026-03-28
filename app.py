from flask import Flask, render_template, request
import password_strength_checker

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods = ["POST"])
def results():
    password = request.form["password"] # Assign password variable to password input from index.html
    # Call check_strength function from password_strength_checker.py and unpack the returned values into variables.
    strength_score, strength_label, color, results = password_strength_checker.check_strength(password) 
    return render_template("results.html", 
                           password=password, 
                           strength_score=strength_score, 
                           strength_label=strength_label, 
                           color=color,
                           results=results)
# TODO: With the results variable, we will change CSS elements to match the
# results of the password strength check. For example if color is red, we change
# something in there to be red, etc. 

if __name__ == "__main__":
    app.run(debug=True)