from flask import Flask

app = Flask(__name__)

@app.route("/info")
def lwinfo():
    return "I am rahul from India"

@app.route("/phone")
def lwphone():
    return "4564134596"

# Only run the server if this file is executed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0")
