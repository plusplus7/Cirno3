class Article():
    def __init__(self, dic):
        self.aid            = dic['aid']
        self.article_id     = dic['article_id']
        self.create_time    = dic['create_time']
        self.view_count     = dic['view_count']
        self.preview        = dic['preview']
        self.content        = dic['content']
