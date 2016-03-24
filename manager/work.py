# coding: utf-8
from base_mangaer import BaseManger
from rules.work import MainPage
from rules.work import NewsPage
from database.Work import WorkDB


class WorkManager(BaseManger):

    def __init__(self, news_base_url):
        BaseManger.__init__(self, base_url='http://job.myclub2.com/',
                            news_base_url=news_base_url, main_page_object=MainPage,
                            news_page_object=NewsPage, database_object=WorkDB)

    def func_news_type(self, url):
        if 'label' in url:
            return int(url[-2:])



