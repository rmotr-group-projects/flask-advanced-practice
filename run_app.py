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
@app.route('/login-form', methods=['GET', 'POST'])
def login_form():
    """
        Reply the examples given above in one single view. You can use request.method
        to determine which HTTP method was used (either 'GET' or 'POST'),
        and perform one action or another.
        
        You’ll work on login_form() view. You’ll have to somehow determine which 
        HTTP method was used (either GET or POST).

        If GET method was used, just return HTML content with the login form. 
        Make sure that the new HTML login form points to the same /login-form URL while POSTing

        If POST method was used, get the given username and password from the form data 
        and perform a redirect to index() view sending the username as payload. 
        NOTE: If any of username or password were not given, use Flask’s abort() 
        function to return a 404 - Not found response
    """
    if request.method == 'GET':
        return get_login_form()
    elif request.method == 'POST':
        try:
            username = request.form['username']
            pw = request.form['password']
        except KeyError:
            abort(404)
        else:
            return redirect(url_for('index'))

# Extra task
# NOTE: Use '/profile' URL for this view
@app.route('/profile')
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
