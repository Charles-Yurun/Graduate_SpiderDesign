from models.Work import Work
from leancloud import Query, LeanCloudError


class WorkDB:

    def __init__(self, **kwargs):
        self.work = Work()
        for k, v in kwargs.items():
            self.work.set(k, v)

    def save(self):
        # try:
        self.work.save()
        # except:
        #     print "Read time Out ---------------------------------------"
        #     self.save()

    def delete(self):
        pass

    @staticmethod
    def is_existed(url):
        try:
            new = Query(Work).equal_to('news_url', url).find()
        except LeanCloudError:
            print "the table not exist"
            return False
        if new:
            return True
        return False
