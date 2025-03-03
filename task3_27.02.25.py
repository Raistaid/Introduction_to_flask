from flask import Flask, url_for, request

app = Flask(__name__)

@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.jpeg')}" 
                        alt="здесь должна была быть картинка марса">
                    <h3>Вот она какая, красная планета<h3>
                  </body>
                </html>"""
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
