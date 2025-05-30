from flask import Flask, url_for, request, render_template, redirect

app = Flask(__name__)


@app.route('/index/<title>')
@app.route('/<title>')
def index(title):
    return render_template('base.html', title=title)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
