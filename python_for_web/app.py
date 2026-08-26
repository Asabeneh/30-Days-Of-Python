# let's import the flask
from flask import Flask, render_template, request, redirect, url_for
import os  # importing operating system module

app = Flask(__name__)
# to stop caching static file
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')  # this decorator create the home route
def home():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = 'Python 30天学习'
    return render_template('home.html', techs=techs, name=name, title='首页')


@app.route('/about')
def about():
    name = 'Python 30天学习'
    return render_template('about.html', name=name, title='关于')


@app.route('/result')
def result():
    return render_template('result.html', title='分析结果')


@app.route('/post', methods=['GET', 'POST'])
def post():
    name = '文本分析'
    if request.method == 'GET':
        return render_template('post.html', name=name, title=name)
    if request.method == 'POST':
        content = request.form['content']
        return redirect(url_for('result'))


if __name__ == '__main__':
    # for deployment
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
