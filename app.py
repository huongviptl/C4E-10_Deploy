import os
from flask import *
import mlab
from mongoengine import *
from werkzeug.utils import secure_filename

app = Flask(__name__)
mlab.connect()

app.config["IMG_PATH"] = os.path.join(app.root_path,"images")
app.secret_key = "Dinh Heo"
class Tobacco(Document):
    image = StringField()
    title = StringField()
    price = FloatField()

tobacco1 = Tobacco(
    image="http://macbarenvietnam.com/wp-content/uploads/2016/05/555_state_express_gold_filter_king_size.jpg",
    title="Tobacco 555",
    price= 30000
)
# tobacco1.save()

# image = "http://cayvahoa.net/wp-content/uploads/2016/04/y-nghia-hoa-oai-huong.jpg"
# title = "Red rose"
# price = 10000

@app.route("/signup")
def add_user():
    user = input('Create Username: ')
    password = input('Create Password: ')

    username.append(user)
    password.append(password)
    if user in login:
        print "That user already exsist"
        return False
    else:
        store[user] = password
        return True

@app.route("/logout")
def logout():
    session["logged_in"] = False
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        form = request.form
        username = form["username"]
        password = form["password"]

        if username == "admin" and password == "admin":
            # Valid credentials
            session["logged_in"] = True
            return redirect(url_for("index"))
        else:
            # Invalid credentials
            return "Invalid credentials"



@app.route('/')
def index():
    return render_template("index.html", Tobacco= Tobacco.objects())

@app.route("/images/<image_name>")
def image(image_name):
    return send_from_directory(app.config["IMG_PATH"], image_name)

@app.route("/add-tobacco", methods=["GET", "POST"])
def add_tobacco():
    if "logged_in" in session and session["logged_in"]:

        if request.method == "GET": # FORM Requested
            return render_template("add_tobacco.html")
        elif request.method == "POST": # user submitted FORM
            # 1: Get data (title, image, price)
            form = request.form
            title = form["title"]
            # image = form["image"]
            price = form["price"]
            image = request.files["image"]

            filename = secure_filename(image.filename)

            image.save(os.path.join(app.config["IMG_PATH"],filename))

            # #2: Save data into database
            new_tobacco = Tobacco(title=title,
                                  image="/images/{0}".format(filename),
                                  price=price)
            new_tobacco.save()
            return redirect(url_for("index"))
    else:
        return redirect(url_for("login"))

@app.route("/aboutme")
def aboutme():
    return render_template("aboutme.html")

@app.route("/users/<username>")
def user(username):
    return "Hello my name is " + username + ", welcome to my page <3"

@app.route("/add/<int:a>/<int:b>")
def add(a,b):
    a = int(a)
    b = int(b)
    return "{0}+{1} = {2}".format(a, b, a+b)

if __name__ == '__main__':
    app.run()
