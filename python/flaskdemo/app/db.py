# -*- coding: utf-8 -*-

import os
import sqlite3
from flask import g

DATABASE = os.path.join(os.path.dirname(__file__), '..', 'db', 'flaskdemo.db')


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_to_database()
    return db


def connect_to_database():
    db = sqlite3.connect(DATABASE)
    return db


def close_connection(exception=None):
    db = getattr(g, '_database', None)
    if db is not None:
        db.commit()
        db.close()
