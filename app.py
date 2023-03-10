import os
from flask import Flask, request, render_template

# pylint: disable=C0103
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"



if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
