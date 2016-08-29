from base_dao import BaseDao
from category import Category
class CategoryDao(BaseDao):
    def get_categories(self):
        sql = 'select * from category'
        self.cursor.execute(sql)
        datas = self.cursor.fetchall()
        result = []
        for data in datas:
            result.append(Category(data))
        return result
