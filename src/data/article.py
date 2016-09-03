class Article():
    def __init__(self, dic = None):
        if dic == None:
            self.aid            = None
            self.article_id     = None
            self.create_time    = None
            self.view_count     = None
            self.preview        = None
            self.content        = None
            return
        else:
            self.aid            = dic['aid']
            self.article_id     = dic['article_id']
            self.create_time    = dic['create_time']
            self.view_count     = dic['view_count']
            self.preview        = dic['preview']
            self.content        = dic['content']
