from models.College import College
from leancloud import Query, LeanCloudError


class CollegeDB:
    def __init__(self, **kwargs):
        self.college = College()
        for k, v in kwargs.items():
            self.college.set(k, v)

    def save(self):
        try:
            self.college.save()
        except:
            print "Read time Out ---------------------------------------"
            self.save()

    def delete(self):
        pass

    @staticmethod
    def is_existed(url):
        try:
            new = Query(College).equal_to('news_url', url).find()
        except LeanCloudError:
            print "the table not exist"
            return False
        if new:
            return True
        return False

