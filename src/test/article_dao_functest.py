import MySQLdb
from article_dao import ArticleDao
import unittest
import datetime
from article import Article

class TestArticleDao(unittest.TestCase):
    def setUp(self):
        self.conn = MySQLdb.connect(host    = 'localhost',
                user    = 'root',
                passwd  = 'root',
                db      = 'cirno_test',
                port    = 3306,
                charset = 'utf8')
        pass
    def tearDown(self):
        pass

    def testGetArticles(self):
        dao = ArticleDao(self.conn)
        a = dao.get_articles()
        a = a[0]
        self.assertEqual(a.aid, 1)
        self.assertEqual(a.article_id, 'test_id')
        self.assertEqual(a.create_time, datetime.datetime(2016, 8, 28, 17, 44, 17))
        self.assertEqual(a.view_count, 2333)
        self.assertEqual(a.preview, 'haha')
        self.assertEqual(a.content, '+1s')

    def testAddArticle(self):
        dao = ArticleDao(self.conn)

        a = Article({
            "aid"           : None,
            "create_time"   : None,
            "article_id"    : "add_test_id",
            "view_count"    : 100,
            "preview"       : "add_test_preview",
            "content"       : "add_test_content",
        })

        result = dao.add_article(a)
        self.assertEqual(result, 1)

        arts = dao.get_articles()
        self.assertEqual(len(arts), 2)

        for i in arts:
            if i.aid != 1:
                self.assertEqual(i.article_id,  "add_test_id")
                self.assertEqual(i.view_count,  100)
                self.assertEqual(i.preview,     "add_test_preview")
                self.assertEqual(i.content,     "add_test_content")

        result = dao.delete_article(a)
        self.assertEqual(result, 1)

        result = dao.delete_article(a)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
