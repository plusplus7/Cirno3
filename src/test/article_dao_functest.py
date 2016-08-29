import MySQLdb
from article_dao import ArticleDao
import unittest
import datetime

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
        dao.open()
        a = dao.get_articles()
        self.assertEqual(len(a), 1)
        a = a[0]
        self.assertEqual(a.aid, 1)
        self.assertEqual(a.article_id, 'test_id')
        self.assertEqual(a.create_time, datetime.datetime(2016, 8, 28, 17, 44, 17))
        self.assertEqual(a.view_count, 2333)
        self.assertEqual(a.preview, 'haha')
        self.assertEqual(a.content, '+1s')
        dao.close()

if __name__ == '__main__':
    unittest.main()
