from flask import Flask, render_template, redirect, request
import model
app = Flask(__name__)

@app.route("/")
def index():
    user_list = model.session.query(model.User).limit(5).all()
    return render_template("user_list.html", users=user_list)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    beans = 5
    return render_template("signup.html", bean = beans)

@app.route("/create_user", methods=['GET', 'POST'])
def create_user():
    print request.form["username"]
    return "Hello"

@app.route("/users")
def show_users():
    user_list = model.session.query(model.User).limit(100).all()
    return render_template("users.html", users=user_list)

@app.route("/users/<int:id>")
def show_profile(id):
    user = model.session.query(model.User).filter_by(id = id).one()
    print user.age
    # list of rating objects by the user
    ratings_list = model.session.query(model.Rating).filter_by(user_id = id).all()
    

    return render_template("user_profile.html", user = user, ratings = ratings_list)

if __name__ == "__main__":
    app.run(debug = True)