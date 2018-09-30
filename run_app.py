import os
from flask import Flask, request, redirect, url_for, abort, render_template

app = Flask(__name__)

@app.route('/')
def home():
    user = request.args.get('user', 'Guido Van Rossum')
    return redirect(url_for('index', user=user))


@app.route('/index')
def index():
    user = request.args.get('user', 'Guido Van Rossum')
    return render_template('index.html', user=user)


@app.route('/get-form', methods=['GET'])
def get_login_form():
    html = """
            <div class="container">
                <form action="/post-form" method="POST">
                  <div class="form-group">
                    <label for="username">Username</label>
                    <input type="text" class="form-control" id="username" placeholder="Your Username">
                  </div>
                  
                   <div class="form-group">
                    <label for="password">Password</label>
                    <input type="password" class="form-control" id="password" placeholder="Your Password">
                  </div> 
                  <button type="submit" class="btn btn-success">Submit</button>
                </form>
            </div>
            """
    return html


@app.route('/post-form', methods=['POST'])
def post_login_form():
    user = request.form['username']
    return redirect(url_for('index', user=user))


@app.route('/login-form', methods=['GET', 'POST'])
def login_form():
    
    if request.method == 'GET':
        return render_template('login_form.html')
        
    elif request.method == 'POST':
        user = request.form.get('username')
        password = request.form.get('password')
        
        if user and password:
            return redirect(url_for('index', user=user))
        
        else:
            return abort(404)  


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

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)