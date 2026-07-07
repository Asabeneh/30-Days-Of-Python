# let's import the flask
from flask import Flask, render_template, request, redirect, url_for, Response
from functools import wraps
import os  # importing operating system module

app = Flask(__name__)

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or auth.password != os.environ.get('APP_PASSWORD', ''):
            return Response('Authentication required.', 401,
                {'WWW-Authenticate': 'Basic realm="Login Required"'})
        return f(*args, **kwargs)
    return decorated
# to stop caching static file
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')  # this decorator create the home route
def home():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30 Days Of Python Programming'
    return render_template('home.html', techs=techs, name=name, title='Home')


@app.route('/about')
def about():
    name = '30 Days Of Python Programming'
    return render_template('about.html', name=name, title='About Us')


@app.route('/result')
def result():
    return render_template('result.html')


@app.route('/post', methods=['GET', 'POST'])
@requires_auth
def post():
    name = 'Text Analyzer'
    if request.method == 'GET':
        return render_template('post.html', name=name, title=name)
    if request.method == 'POST':
        content = request.form['content']
        return redirect(url_for('result'))


if __name__ == '__main__':
    # for deployment
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    app.run(debug=debug, host='127.0.0.1', port=port)
