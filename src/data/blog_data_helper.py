from article_dao import ArticleDao
from category_dao import CategoryDao

class BlogDataHelper():
    def __init__(self, connection):
        self.article_dao    = ArticleDao(connection)
        self.category_dao   = CategoryDao(connection)

    def open(self):
        self.article_dao.open()
        self.category_dao.open()
        self.load()

    def close(self):
        self.article_dao.close()
        self.category_dao.close()

    def load(self):
        self.articles   = self.article_dao.get_articles()
        self.categories = self.category_dao.get_categories()

    def get_articles(self):
        return self.articles

    def get_categories(self):
        return self.categories
