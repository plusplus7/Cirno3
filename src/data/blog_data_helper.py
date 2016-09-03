from article_dao    import ArticleDao
from category_dao   import CategoryDao
from article        import Article
from category       import Category
import json

class BlogDataHelper():
    def __init__(self, connection):
        self.article_dao    = ArticleDao(connection)
        self.category_dao   = CategoryDao(connection)
        self.articles       = None
        self.categories     = None
        self.article_map    = {}
        self.category_map   = {}
        self.category_list_map     = {}
        self.category_type_map     = {}

    def open(self):
        self.load()

    def close(self):
        pass

    def load(self):
        article_map_new         = {}
        category_map_new        = {}
        category_list_map_new   = {}
        category_type_map_new   = {}

        self.articles   = self.article_dao.get_articles()
        self.categories = self.category_dao.get_categories()
        for article in self.articles:
            article_map_new[article.article_id] = article

        for category in self.categories:
            category_map_new[category.category_id] = category
            article_list = []
            for article_id in json.loads(category.article_list.replace('\'', '\"')):
                article_list.append(article_map_new[article_id])
            category_list_map_new[category.category_id] = article_list

            if category.sector_id not in category_type_map_new:
                category_type_map_new[category.sector_id] = {}

            
            if category.category_type not in category_type_map_new[category.sector_id]:
                category_type_map_new[category.sector_id][category.category_type] = []
            category_type_map_new[category.sector_id][category.category_type].append(category)

        self.article_map        = article_map_new
        self.category_map       = category_map_new
        self.category_list_map  = category_list_map_new
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
        return self.category_list_map[category_id]

    def get_categories_for_admin(self):
        result = {}
        for category in self.categories:
            result[category.category_id] = {
                "articles"  : json.loads(category.article_list.replace('\'', '\"')),
                "name"      : category.display_name,
                "sector"    : category.sector_id,
                "type"      : category.category_type,
            }
        return json.dumps(result)

    def add_article(self, article_id, preview, content):
        a = Article()
        a.article_id    = article_id
        a.preview       = preview
        a.content       = content
        a.view_count    = 0
        return self.article_dao.add_article(a)

    def add_category(self, category_id, display_name, sector_id, category_type):
        c = Category()
        c.category_id   = category_id
        c.display_name  = display_name
        c.sector_id     = sector_id
        c.category_type = category_type

        return self.category_dao.add_category(c)

    def attach_article_to_category(self, article_id, category_id):
        c = self.category_map[category_id]
        al = json.loads(c.article_list.replace('\'', '\"'))
        al.insert(0, article_id)
        c.article_list = json.dumps(al)
        return self.category_dao.update_category(c)
