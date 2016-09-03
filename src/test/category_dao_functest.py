import MySQLdb
from category_dao import CategoryDao
import unittest
import datetime
import json

class TestCategoryDao(unittest.TestCase):
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

    def testGetCategory(self):
        dao = CategoryDao(self.conn)
        dao.open()
        a = dao.get_categories()
        self.assertEqual(len(a), 1)
        a = a[0]
        self.assertEqual(a.cid, 1)
        self.assertEqual(a.category_id, 'test_id')
        self.assertEqual(a.display_name, 'test_display_id')
        self.assertEqual(a.sector_id, 'game')
        self.assertEqual(a.category_type, 'top')
        self.assertEqual(a.article_list, "['test_id']")

    def testUpdateCategory(self):
        dao = CategoryDao(self.conn)
        dao.open()
        a = dao.get_categories()
        self.assertEqual(len(a), 1)
        a = a[0]
        self.assertEqual(a.cid, 1)
        self.assertEqual(a.category_id, 'test_id')
        self.assertEqual(a.display_name, 'test_display_id')
        self.assertEqual(a.sector_id, 'game')
        self.assertEqual(a.category_type, 'top')
        al = json.loads(a.article_list.replace('\'', '\"'))
        self.assertEqual(len(al), 1)
        self.assertTrue("test_id" in al)
        
        al.append("hahah")
        a.article_list = json.dumps(al)
        print a.article_list
        result = dao.update_category(a)
        self.assertEqual(result, 1)

        a = dao.get_categories()
        self.assertEqual(len(a), 1)
        a = a[0]
        self.assertEqual(a.cid, 1)
        self.assertEqual(a.category_id, 'test_id')
        self.assertEqual(a.display_name, 'test_display_id')
        self.assertEqual(a.sector_id, 'game')
        self.assertEqual(a.category_type, 'top')

        al = json.loads(a.article_list.replace('\'', '\"'))
        self.assertEqual(len(al), 2)
        self.assertTrue("test_id" in al)
        self.assertTrue("hahah" in al)

        al = ["test_id"]
        a.article_list = json.dumps(al)
        print a.article_list
        result = dao.update_category(a)
        self.assertEqual(result, 1)

        a = dao.get_categories()
        self.assertEqual(len(a), 1)
        a = a[0]
        self.assertEqual(a.cid, 1)
        self.assertEqual(a.category_id, 'test_id')
        self.assertEqual(a.display_name, 'test_display_id')
        self.assertEqual(a.sector_id, 'game')
        self.assertEqual(a.category_type, 'top')
        self.assertEqual(len(al), 1)
        self.assertTrue("test_id" in al)

if __name__ == '__main__':
    unittest.main()
