from base_dao import BaseDao
from article  import Article

class ArticleDao(BaseDao):
    def get_articles(self):
        sql = 'select * from article'
        self.cursor.execute(sql)
        datas = self.cursor.fetchall()
        result = []
        for data in datas:
            result.append(Article(data))
        return result
