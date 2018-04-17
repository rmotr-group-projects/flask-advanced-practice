import os
from flask import Flask, request, redirect, url_for


app = Flask(__name__)

@app.route('/index')
def index():
    user = request.args.get('user') or 'Guido Van Rossum'
    html = """
        <html>
            <h1>Hello {}!</h1>
        </html>
    """.format(user.title())
    return html


@app.route('/get-form', methods=['GET'])
def get_login_form():
    html = """
        <form action="/post-form" method="POST">
            <div>
                <label>Username</label>
                <input name="username">
            </div>
            <div>
                <label>Password</label>
                <input name="password" type="password">
            </div>
            <button type="submit">Submit</button>
        </form>
    """
    return html


@app.route('/post-form', methods=['POST'])
def post_login_form():
    user = request.form['username']
    return redirect(url_for('index', user=user))


@app.route('/login-form', methods=['GET', 'POST'])
def login_form():
    """
        Reply the examples given above in one single view. You can use request.method
        to determine which HTTP method was used (either 'GET' or 'POST'),
        and perform one action or another.
    """
    pass


if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)
