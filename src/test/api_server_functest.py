# -*- coding: UTF-8 -*-

import hashlib
import hmac
import time
import unittest
import urllib
import urllib2

class ApiServerSdk():

    def __init__(self, host, id, key):
        self.host   = host
        self.id     = id
        self.key    = key
        self.vers   = "1.0" 

    def sign(self, method, params):
        s = params.keys()
        s.sort()
        tosign =  method + "|"
        for i in s:
            tosign = tosign + ("%s=%s|" % (i, params[i]))
        tosign = tosign[:-1]
        return hmac.new(self.key, tosign, hashlib.sha1).digest().encode("base64").rstrip('\n')

    def invoke_method(self, method, params):
        params["Action"]    = method
        params["Key"]       = self.id
        params["Timestamp"] = str(int(time.time()))
        params["Version"]   = self.vers
        params["Signature"] = self.sign("POST", params)

        url = "http://%s/api/%s" % (self.host, method)
        res = None
        try:
            res = urllib2.urlopen(url, urllib.urlencode(params))
        except urllib2.HTTPError as e:
            return e.read()
        return res.read()

    def create_article(self, article_id, category_id, preview, content):
        params = {}
        params["ArticleId"]     = article_id
        params["CategoryId"]    = category_id
        params["Preview"]       = preview
        params["Content"]       = content 
        return self.invoke_method("CreateArticle", params)

    def create_category(self, category_id, display_name, section_id, type):
        params = {}
        params["CategoryId"]    = category_id
        params["DisplayName"]   = display_name
        params["SectionId"]     = section_id
        params["Type"]          = type
        return self.invoke_method("CreateCategory", params)

    def attach_article_to_category(self, article_id, category_id):
        params = {}
        params["ArticleId"]     = article_id
        params["CategoryId"]    = category_id
        return self.invoke_method("AttachArticleToCategory", params)

class TestApiServer(unittest.TestCase):

    def setUp(self):
        self.c = ApiServerSdk("localhost:8080", "test", "test")

    def testCreateArticle(self):
        print self.c.create_article("test_dididi", "index", "prrrr", "conttttt")

    def testCreateCategory(self):
        print self.c.create_category("test_cate", "test_display", "game", "top")

    def testAttachArticleToCategory(self):
        print self.c.attach_article_to_category("test_dididi", "test_cate")

    def testAll(self):
        print self.c.create_article("test_art_all_1", "index", "prrrr", "conttttt")
        print self.c.create_category("test_cate_all_1", "test_display", "game", "top")
        print self.c.attach_article_to_category("test_art_all_1", "test_cate_all_1")

if __name__ == "__main__":
    unittest.main()
