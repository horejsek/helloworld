# -*- coding: utf-8 -*-

from flask import Flask

from app.db import close_connection
from article import article_page


app = Flask(__name__)
app.teardown_appcontext(close_connection)

app.register_blueprint(article_page)

if __name__ == '__main__':
    app.run(debug=True)
