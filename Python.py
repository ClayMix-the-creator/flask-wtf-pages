from flask import Flask, render_template


app = Flask(__name__)


# @app.route('/.../<str>/<int:...>/<float:...>')
# <p><a href=""> </a></p>

@app.route('/')
def start_page():
    return """<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Стартовая страница</title>
                      </head>
                      <body>
                        <p><a href="/">Стартовая страница</a></p>
                        <p><a href="index/...">Готовимся к миссии</a></p>
                      </body>
                    </html>"""


@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
