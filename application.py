import os

from flask import Flask, session, render_template, request,
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/", methods=["GET", "POST"])
def index():

## If not logged in - move to login page (and register)
	if session.get("user_id") is None:
		return render_template("login.html")
	if request.method == "POST":
		user_id = request.form.get("user_id")
## Search book by: ISBN, TITLE, AUTHOR
	book_title = request.form.get("book_title")
	book_author = request.form.get("book_author")
	book_isbn = request.form.get("book_isbn")

## Redirects to book page

return "Project 1: TODO"

@app.route("/register")
def index():
    return "Project 1: TODO"


@app.route("/login")
def index():
    return "Project 1: TODO"


@app.route("/search_results")
def index():
    return "Project 1: TODO"



@app.route("/books/<int:book_isbn>")
def index():
    return "Project 1: TODO"




@app.route("/api/<isbn>")
def index():
    return "Project 1: TODO"