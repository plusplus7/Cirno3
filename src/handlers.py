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

class ApiServerHandler(BaseHandler):
    def initialize(self, db):
        super(ApiServerHandler, self).initialize(db)
        self.method_map = {
            "ListCategories" : self.list_categories,
            "CreateArticle"  : self.add_article,
            "CreateCategory" : self.add_category,
        }
        self.basic_parameters = ["Action", "AccessKeyId", "SignatureMethod", "SignatureVersion", "Timestamp", "Version"]
        self.parameter_map = {
            "ListCategories"    : [],
            "CreateArticle"     : ["ArticleId", "Category", "Preview", "Content"],
            "CreateCategory"    : ["CategoryId", "CategoryDisplayName", "SectionId", "Type"],
        }

    def invoke_api(self, method):
        context = {}
        for param in self.basic_parameters:
            res = self.get_arguments(param)
            if len(res) == 0:
                return (404, "MissingParameter.%s" % param)
            context[param] = res[0]

        if cmp(context["Action"], method) != 0:
            return (403, "MethodNotAllowed.%s", context["Action"])

        for param in self.parameter_map[method]:
            res = self.get_arguments(param)
            if len(res) == 0:
                return (404, "MissingParameter.%s" % param)
            context[param] = res[0]

        self.method_map[method](context)

    def add_article(self, context):
        self.db.add_article(context["ArticleId"], context["Preview"], context["Content"])
        self.db.attach_article_to_category(context["ArticleId"], context["Category"])
        self.db.load()

    def add_category(self, context):
        self.db.add_category(context["CategoryId"], context["CategoryDisplayName"], context["SectionId"], context["Type"])
        self.db.load()
        pass

    def list_categories(self, context):
        self.write(self.db.get_categories_for_admin())

    def post(self, method):
        if method in self.method_map:
            self.invoke_api(method)
        else:
            self.write(json.dumps({
                "ErrorCode" : "404",
                "ErrorMessage" : "Unknown method",
                }
            ))
