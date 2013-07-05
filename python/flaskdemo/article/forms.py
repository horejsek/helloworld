# -*- coding: utf-8 -*-

from wtforms import Form, TextField, TextAreaField, validators


class ArticleForm(Form):
    title = TextField('Title', [validators.Length(min=4, max=50)])
    text = TextAreaField('Text')
