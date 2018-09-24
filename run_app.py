import os
from flask import Flask, request, redirect, url_for, abort, render_template


app = Flask(__name__)

@app.route('/index')
def index():
    user = request.args.get('user', 'Guido Van Rossum')
    html = """
        <html>
            <h1>Hello {}!</h1>
        </html>
    """.format(user.title())
    return html


@app.route('/get-form', methods=['GET'])
def get_login_form():
    return render_template('login_form.html')


@app.route('/post-form', methods=['POST'])
def post_login_form():
    user = request.form.get('username')
    return redirect(url_for('index', user=user))


# NOTE: Use '/login-form' as URL for this view in order to make tests pass
@app.route('/login-form', methods=['GET', 'POST'])
def login_form():
    http_method = request.method
    if (http_method == 'GET'):
        return render_template('login_form.html')
    elif (http_method == 'POST'):
        #if ('username' in request.form.keys() and 'password' in request.form.keys()):
        user = request.form.get('username', None)
        password = request.form.get('password', None)
        if (user is None) or (password is None):
            return abort(404)     
        else:
            return redirect(url_for('index', user=user))  


# Extra task
# NOTE: Use '/profile' URL for this view
@app.route('/profile', methods=['GET'])
def profile():
    """
        For this task, we'll create a user profile using the USER_DATA given below.
        The structure of the HTML code is given to you inside a folder
        called "templates" (in which Flask looks for templates by default).
        Some of the data was completed inside the template for you as example,
        make sure to complete the rest.
        You'll also have to render the 'profile.html' file using the render_template()
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
    return render_template('profile.html', user_data=USER_DATA)


if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)
