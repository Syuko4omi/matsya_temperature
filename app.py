import os

from flask import Flask

from matsya_temperature.generate_sentence import generate_sentence

app = Flask(__name__)


@app.route("/")
def matsya_report_temperature():
    return generate_sentence()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
