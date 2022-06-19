import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"<p>Hello, did you know I may be running on AWS rn ?<br>Version: {os.environ.get('APP_VERSION')}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
