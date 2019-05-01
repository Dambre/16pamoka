
from flask import Flask, render_template, make_response, request
from datetime import datetime, timedelta


app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    response = make_response(render_template('index.html'))
    response.set_cookie("user_name", expires=0)
    return response


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        response = make_response(
            render_template("login-success.html", username=username),
        )
        expiration_day = datetime.now() + timedelta(days=10)
        response.set_cookie("username", username, expires=expiration_day)
        return response
    else:
        return render_template('/login.html')


@app.route('/about-me')
def about_me():
    now = datetime.now()
    return render_template('about_me.html', dabar=now)


@app.route('/portfolio')
def portfolio():
    now = datetime.now()
    return render_template('portfolio.html', dabar=now)


if __name__ == '__main__':
    app.run(debug=True)
