from flask import Flask, request, jsonify
from flask.templating import render_template
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)


@app.route("/users")
def users():
    try:
        conn = sqlite3.connect("test.db")
        return jsonify(conn.execute("SELECT * FROM users").fetchall())
    except Exception as e:
        return "ERROR: " + str(e)

@app.route("/new_user", methods=["POST"])
def new_user():
    if request.method == "POST":
        try:
            # handle the form
            username = request.form['username']
            id = request.form['id']
            balance = request.form['balance']
            email = request.form['email']

            # execute SQL statement and commit to the database
            conn = sqlite3.connect("test.db")
            conn.execute(f"INSERT INTO users VALUES ({id}, '{username}', {balance}, '{email}')")
            conn.commit()

            # if nothing goes wrong return "success"
            return "success"
        except Exception as e:
            return "ERROR: " + str(e)
    else:
        return "Try using a POST request with this endpoint."

@app.route("/")
def index():
    return render_template("index.html")

