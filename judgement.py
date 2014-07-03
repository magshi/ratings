from flask import Flask, render_template, redirect, request, flash
import model

app = Flask(__name__)

@app.route("/")
def index():
    user_list = model.session.query(model.User).limit(5).all()
    return render_template("user_list.html", users=user_list)

@app.route("/signup", methods=['GET'])
def signup():
    return render_template("signup.html")

@app.route("/signup", methods=['POST'])
def process_signup():
    user = model.User(email = request.form.get('email'),
                password = request.form.get('password'),
                age = request.form.get('age'),
                zipcode = request.form.get('zipcode'),
                gender = request.form.get('gender'),
                occupation = request.form.get('occupation'))

    print user.email, user.password, user.zipcode, user.gender, user.occupation

    model.session.add(user)
    model.session.commit()
    flash("Thank you for your information!")
    return redirect("/")

@app.route("/login", methods=['GET'])
def login():
    return render_template("login.html")

@app.route("/login", methods=['POST'])
def process_login():
    pass

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

app.secret_key = """\xed\x8b\xcf^L\xb1\xf5\x12'\xcc\xb9\xeb<\xefL\xd8\x15c0\x1e=kz;"""

if __name__ == "__main__":
    app.run(debug = True)