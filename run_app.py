import os
from flask import Flask, request, redirect, url_for, abort, render_template


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


# NOTE: Use '/login-form' as URL for this view in order to make tests pass
def login_form():
    """
        Reply the examples given above in one single view. You can use request.method
        to determine which HTTP method was used (either 'GET' or 'POST'),
        and perform one action or another.
    """
    pass


# Optional extra task
# NOTE: Use '/profile' URL for this view
def profile():
    """
        For this optional task, you'll have to create a user profile using the
        data given below. In order to do that, you'll need to create a new
        'profile.html' file with your HTML code, inside a new folder
        called "templates" (in which Flask looks for templates by default).
        Once the HTML code is implemented, render it using the "render_template()"
        function imported from Flask, and send the user data as context.
    """
    USER_DATA = {
        'first_name': 'Guido',
        'last_name': 'van Rossum',
        'age': 62,
        'birthdate': '31 January 1956',
        'nationality': 'Dutch',
        'worked_at': [
            'Python language development',
            'Google',
            'Dropbox'
        ]
    }
    pass


if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)
