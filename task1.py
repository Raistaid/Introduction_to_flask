from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/sample_page')
def return_sample_page():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Задание Яндекс лицей</title>
                  </head>
                  <body>
                    <h1>Миссия Колонизация Марса</h1>
                  </body>
                </html>"""

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
