#-*- coding: UTF-8 -*-
import json
from Crypto.Cipher import AES
import time
import base64
import uuid
import tornado.web
import tornado.gen

class BaseHandler(tornado.web.RequestHandler):
    def initialize(self, db):
        self.db = db

class IndexHandler(BaseHandler):
    def get(self):
        self.render("index.html")

class BlogIndexHandler(BaseHandler):
    def get(self, area_id = "index"):
        categories = self.db.get_article_by_category_id(area_id)
        if categories == None:
            self.render("error_page.html", error_info = "Unknown area_id %s" % area_id)

        self.render("blog_index.html",
            area_list   = self.db.get_category_by_category_type("blog", "common"),
            prev_list   = categories,
            side_list   = self.db.get_category_by_category_type("blog", "side"),
            top_list    = self.db.get_category_by_category_type("blog", "top"),
        )

class BlogMainHandler(BaseHandler):
    def get(self, post_id):
        article = self.db.get_article_by_article_id(post_id)
        if article == None:
            self.render("error_page.html", error_info = "Unknown post_id %s" % post_id)

        self.render("blog_main.html",
            article     = article,
            top_list    = self.db.get_category_by_category_type("blog", "top"),
            )

class GameIndexHandler(BaseHandler):
    def get(self, area_id = "gameindex"):
        categories = self.db.get_article_by_category_id(area_id)
        if categories == None:
            self.render("error_page.html", error_info = "Unknown area_id %s" % area_id)

        self.render("game_index.html",
            area_list   = self.db.get_category_by_category_type("game", "common"),
            prev_list   = categories,
            side_list   = self.db.get_category_by_category_type("game", "side"),
            top_list    = self.db.get_category_by_category_type("game", "top"),
        )

class GameMainHandler(BaseHandler):
    def get(self, post_id):
        article = self.db.get_article_by_article_id(post_id)
        if article == None:
            self.render("error_page.html", error_info = "Unknown post_id %s" % post_id)

        self.render("game_main.html",
            article     = article,
            top_list    = self.db.get_category_by_category_type("game", "top"),
        )
