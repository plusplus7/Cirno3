import tornado.web
import tornado.options
import logging
import tornado.ioloop
import os
import MySQLdb
from handlers import *
from blog_data_helper import BlogDataHelper

connection = MySQLdb.connect(
    host    = 'localhost',
    user    = 'root',
    passwd  = 'root',
    db      = 'cirno',
    port    = 3306,
    charset = 'utf8'
)
db = BlogDataHelper(connection)

urls = [
    (r'/', IndexHandler, dict(db=db)),
    (r'/game', GameIndexHandler, dict(db=db)),
    (r'/game/area/(?P<area_id>[a-zA-Z0-9-_]+)', GameIndexHandler, dict(db=db)),
    (r'/game/post/(?P<post_id>[a-zA-Z0-9-_]+)', GameMainHandler, dict(db=db)),
    (r'/blog', BlogIndexHandler, dict(db=db)),
    (r'/blog/area/(?P<area_id>[a-zA-Z0-9-_]+)', BlogIndexHandler, dict(db=db)),
    (r'/blog/post/(?P<post_id>[a-zA-Z0-9-_]+)', BlogMainHandler, dict(db=db)),
    (r"/storage", tornado.web.RedirectHandler, {"url": "/blog/post/storage"}),
    (r"/donation", tornado.web.RedirectHandler, {"url": "/blog/post/donation"}),
    (r"/aboutme", tornado.web.RedirectHandler, {"url": "/blog/post/aboutme"}),
]

settings = {
    "static_path"   : os.path.join(os.path.dirname(__file__), "static"),
    "template_path" : os.path.join(os.path.dirname(__file__), "templates"),
    "debug"         : False,
    "gzip"          : True,
}

def main(host="0.0.0.0", port=8080):
    db.open()
    app = tornado.web.Application(urls, **settings)
    app.listen(port, host)
    tornado.ioloop.IOLoop.instance().start()
    db.close()

if __name__ == "__main__":
    main()
