from base_dao import BaseDao
from article  import Article

class ArticleDao(BaseDao):
    def get_articles(self):
        sql = 'select * from article'

        cursor = self.open()
        cursor.execute(sql)
        datas = cursor.fetchall()
        self.close(cursor)

        result = []
        for data in datas:
            result.append(Article(data))
        return result

    def add_article(self, article):
        sql = """
            insert into
                article(article_id, create_time, view_count, preview, content)
                value(%s, now(), %s, %s, %s)
        """

        cursor = self.open()
        cursor.execute(sql, (
            article.article_id,
            article.view_count,
            article.preview,
            article.content))
        self.commit()
        result = cursor.rowcount
        self.close(cursor)

        return result

    def delete_article(self, article):
        sql = """
            delete from article where article_id = %s
        """

        cursor = self.open()
        cursor.execute(sql, (
            article.article_id,
        )) 
        self.commit()
        result = cursor.rowcount
        self.close(cursor)

        return result
