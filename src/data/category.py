class Category():
    def __init__(self, dic):
        self.cid            = dic['cid']
        self.category_id    = dic['category_id']
        self.display_name   = dic['display_name']
        self.sector_id      = dic['sector_id']
        self.category_type  = dic['category_type']
        self.article_list   = dic['article_list']
