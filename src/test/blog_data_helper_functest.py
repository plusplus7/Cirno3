from blog_data_helper import BlogDataHelper
import MySQLdb
import unittest
import datetime

class TestBlogDataHelper(unittest.TestCase):
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
        b = BlogDataHelper(self.conn)
        b.open()
        self.assertEqual(len(b.get_articles()), 1)
        a = b.get_articles()[0]
        self.assertEqual(a.aid, 1)
        self.assertEqual(a.article_id, 'test_id')
        self.assertEqual(a.create_time, datetime.datetime(2016, 8, 28, 17, 44, 17))
        self.assertEqual(a.view_count, 2333)
        self.assertEqual(a.preview, 'haha')
        self.assertEqual(a.content, '+1s')
        b.close()

    def testGetCategory(self):
        b = BlogDataHelper(self.conn)
        b.open()
        self.assertEqual(len(b.get_categories()), 1)
        a = b.get_categories()[0]
        self.assertEqual(a.cid, 1)
        self.assertEqual(a.category_id, 'test_id')
        self.assertEqual(a.display_name, 'test_display_id')
        self.assertEqual(a.sector_id, 'game')
        self.assertEqual(a.category_type, 'top')
        self.assertEqual(a.article_list, "['test_id']")
        b.close()

if __name__ == "__main__":
    unittest.main()
