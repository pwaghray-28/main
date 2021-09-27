from flask import Flask, jsonify
from data import data
app = Flask(__name__)
@app.route("/")
def index():
    return jsonify({
        "data":data
    }),200
if __name__ == "__main__":
    app.run()