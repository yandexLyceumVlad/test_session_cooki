import os
import datetime

from flask import Flask, request, make_response, session

app = Flask(__name__)

@app.route("/")
def index():
    visits_count = session.get('visits_count', 0)
    session['visits_count'] = visits_count + 1
    return make_response(
        f"Вы пришли на эту страницу {visits_count + 1} раз")


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.secret_key = os.urandom(24)
    app.run(host='0.0.0.0', port=port)