from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/promotion')
def promotion():
    lst = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
           'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return '</br>'.join(lst)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
