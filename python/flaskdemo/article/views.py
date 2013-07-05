# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, request, redirect, url_for
import sqlpuzzle

from app.db import get_db
from forms import ArticleForm

article_page = Blueprint('article_page', __name__, template_folder='templates')


@article_page.route('/')
def articles():
    cur = get_db().cursor()
    cur.execute(str(sqlpuzzle.select('id', 'title').from_('article')))
    rows = cur.fetchall()
    articles = [{'id': row[0], 'title': row[1]} for row in rows]
    return render_template('article/list.html', articles=articles)


@article_page.route('/article/<article_id>')
def article(article_id):
    cur = get_db().cursor()
    cur.execute(str(sqlpuzzle.select('title', 'text').from_('article').where({'id': article_id})))
    row = cur.fetchone()
    article = {
        'title': row[0],
        'text': row[1],
    }
    return render_template('article/detail.html', article=article)


@article_page.route('/article/add', methods=['GET', 'POST'])
def add_article():
    form = ArticleForm(request.form)
    if request.method == 'POST' and form.validate():
        sql = sqlpuzzle.insert_into('article').values({
            'title': form.title.data,
            'text': form.text.data,
        })
        cur = get_db().cursor()
        cur.execute(str(sql))
        return redirect(url_for('article_page.articles'))
    return render_template('article/add.html', form=form)
