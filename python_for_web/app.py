# let's import the flask
from flask import Flask, render_template, request, redirect, url_for
import os  # importing operating system module

app = Flask(__name__)
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
def post():
    name = 'Text Analyzer'
    if request.method == 'GET':
        return render_template('post.html', name=name, title=name)
    if request.method == 'POST':
        # request.form.get() returns None instead of raising BadRequestKeyError,
        # so a missing field yields an explicit 400 rather than a 500 traceback.
        content = request.form.get('content')
        if content is None:
            return render_template('post.html', name=name, title=name), 400
        return redirect(url_for('result'))


if __name__ == '__main__':
    # This is the Flask development server. It must NOT be used to serve
    # production traffic, and the Werkzeug debugger must never be enabled on a
    # host reachable by others: the debugger exposes a console that executes
    # arbitrary Python.
    #
    # - debug is opt-in via FLASK_DEBUG=1 and defaults to off;
    # - the default bind address is loopback (127.0.0.1); set HOST explicitly
    #   only when you understand the exposure.
    port = int(os.environ.get("PORT", 5000))
    host = os.environ.get("HOST", "127.0.0.1")
    debug = os.environ.get("FLASK_DEBUG") == "1"
    app.run(debug=debug, host=host, port=port)
