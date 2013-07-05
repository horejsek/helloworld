# -*- coding: utf-8 -*-

import cherrypy


class AppRoot(object):
    def index(self):
        return (
            '<h1>Hello World!</h1>'
            '<p>'
            'I wanted with CherryPy do same demo as is djangodemo. But it '
            'needed so many coding, so I deleted what I had and I leaved here '
            'only this primitive Hello World message. Sorry!'
            '</p>'
        )
    index.exposed = True


if __name__ == '__main__':
    cherrypy.quickstart(AppRoot())
