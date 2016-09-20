from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Home page"

@app.route("/classwork")
def cw():
    return "Classwork page"

@app.route("/homework")
def hw():
    return "Homework page"

if __name__ == "__main__":
    app.run()
