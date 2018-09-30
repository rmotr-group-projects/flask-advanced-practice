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
    return render_template('login_form.html')
    


@app.route('/post-form', methods=['POST'])
def post_login_form():
    user = request.form['username']
    return redirect(url_for('index', user=user))


@app.route('/login-form', methods=['POST', 'GET'])
def login_form():
    if request.method == 'GET':
        return render_template('login_form.html')
        
    elif request.method == 'POST':
        user = request.form.get('username')
        password = request.form.get('password')
        
        if user and password:
            return post_login_form()
        else:
            abort(404)




@app.route('/profile', methods=['GET'])
def profile():
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