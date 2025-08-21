from flask import Flask
from markupsafe import escape

app = Flask(__name__)

# static route
@app.route("/")
def index():
    return "<h1>Hello, World!<h1>"

@app.route("/about")
def about():
    return "<h1>About Page</h1>"

@app.route("/contact")
def contact():
    return "<h1>Contact Page</h1>"

# dynamic route
@app.route("/profile", defaults={"_route": "home", "username": "Guess"}) # default parameter
@app.route("/profile/<string:username>", defaults={"_route": "profile"})
def profile_name(username, _route):
    if _route == "home":
        return f"<h1>Profile Home Page of {username}</h1>"
    elif _route == "profile":
        return f"<h1>Profile Page of {username}</h1>"

@app.route('/htmlescape/<code>')
def html_escape(code):
    return escape(code)

if __name__ == "__main__":
    app.run(debug=True)
