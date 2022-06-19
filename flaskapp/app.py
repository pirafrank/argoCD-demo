from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, did you know I may be running on AWS rn ?</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0")

