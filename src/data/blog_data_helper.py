from article_dao import ArticleDao
from category_dao import CategoryDao
import json

class BlogDataHelper():
    def __init__(self, connection):
        self.article_dao    = ArticleDao(connection)
        self.category_dao   = CategoryDao(connection)
        self.articles       = None
        self.categories     = None
        self.article_map    = {}
        self.category_map   = {}
        self.category_type_map     = {}

    def open(self):
        self.article_dao.open()
        self.category_dao.open()
        self.load()

    def close(self):
        self.article_dao.close()
        self.category_dao.close()

    def load(self):
        article_map_new     = {}
        category_map_new    = {}
        category_type_map_new      = {}

        self.articles   = self.article_dao.get_articles()
        self.categories = self.category_dao.get_categories()
        for article in self.articles:
            article_map_new[article.article_id] = article

        for category in self.categories:
            article_list = []
            for article_id in json.loads(category.article_list.replace('\'', '\"')):
                article_list.append(article_map_new[article_id])
            category_map_new[category.category_id] = article_list

            if category.sector_id not in category_type_map_new:
                category_type_map_new[category.sector_id] = {}

            
            if category.category_type not in category_type_map_new[category.sector_id]:
                category_type_map_new[category.sector_id][category.category_type] = []
            category_type_map_new[category.sector_id][category.category_type].append(category)

        self.article_map        = article_map_new
        self.category_map       = category_map_new
        self.category_type_map  = category_type_map_new

    def get_articles(self):
        return self.articles

    def get_categories(self):
        return self.categories

    def get_article_by_article_id(self, article_id):
        return self.article_map[article_id]

    def get_category_by_category_type(self, sector_id, category_type):
        return self.category_type_map[sector_id][category_type]

    def get_article_by_category_id(self, category_id):
        return self.category_map[category_id]
