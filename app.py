from flask import Flask, escape, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    name = "michael"
    return render_template("admin.html", name=name)

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run()