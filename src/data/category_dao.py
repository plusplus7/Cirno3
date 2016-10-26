from base_dao import BaseDao
from category import Category

class CategoryDao(BaseDao):
    def get_categories(self):
        sql = 'select * from category'

        cursor = self.open()
        cursor.execute(sql)
        datas = cursor.fetchall()
        self.close(cursor)

        result = []
        for data in datas:
            result.append(Category(data))
        return result

    def add_category(self, category):
       sql = """
        insert into
            category(category_id, display_name, sector_id, category_type, article_list)
            value(%s, %s, %s, %s, %s)
       """

       cursor = self.open()
       cursor.execute(sql, (
           category.category_id,
           category.display_name,
           category.sector_id,
           category.category_type,
           '[]'
       ))
       self.commit()
       result = cursor.rowcount
       self.close(cursor)

       return result

    def update_category(self, category):
        sql = """
            update category set
                display_name  = %s,
                sector_id     = %s,
                category_type = %s,
                article_list  = %s
            where category_id = %s
        """

        cursor = self.open()
        cursor.execute(sql, (
            category.display_name,
            category.sector_id,
            category.category_type,
            category.article_list,
            category.category_id
            )
        )
        self.commit()
        result = cursor.rowcount
        self.close(cursor)

        return result
