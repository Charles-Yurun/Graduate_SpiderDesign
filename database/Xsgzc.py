from models.Xsgzc import Xsgzc
from leancloud import Query, LeanCloudError


class XsgzcDB:

    def __init__(self, **kwargs):
        self.xsgzc = Xsgzc()
        for k, v in kwargs.items():
            self.xsgzc.set(k, v)

    def save(self):
        # try:
        self.xsgzc.save()
        # except:
        #     print "Read time Out ---------------------------------------"
        #     self.save()

    def delete(self):
        pass

    @staticmethod
    def is_existed(url):
        try:
            new = Query(Xsgzc).equal_to('news_url', url).find()
        except LeanCloudError:
            print "the table not exist"
            return False
        if new:
            return True
        return False

