from flask import Flask, request, render_template
from markupsafe import escape

app = Flask(__name__)

# static route
@app.route("/")
def index():
    hobbies = ["coding", "reading", "gaming"]
    bio = {"name": "klonggrok", "age": 20, "address": "123 Main St"}
    return render_template("index.html", name="klonggrok", age=20, hobbies=hobbies, bio=bio) 
    # index.html must exists in the templates folder

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

@app.route("/routewithoutslash")
def route_without_slash():
    return "<h1>This route does not end with a slash</h1><hr><p>so if you put a slash at the end, it will show 404 not found!.</p>"

@app.route("/routewithslash/")
def route_with_slash():
    return "<h1>This route ends with a slash</h1><hr><p>No matter you put or not put a slash at the end, it will redirect to this route.</p>"

@app.route("/tryrequest/", methods=["GET", "POST"])
def tryrequest():
    if request.method == "GET":
        return "<h1>GET request received!</h1>" +  request.args.get("name")
    elif request.method == "POST":
        return "<h1>POST request received!</h1>" + request.form["name"]

if __name__ == "__main__":
    app.run(debug=True)
