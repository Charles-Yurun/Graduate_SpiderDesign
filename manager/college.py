# -*- coding: UTF-8 -*-
from base_mangaer import BaseManger
from database.College import CollegeDB
from rules.college import MainPage
from rules.college import NewsPage


class CollegeManger(BaseManger):

    def __init__(self, news_base_url):
        BaseManger.__init__(self, base_url='http://www.guet.edu.cn', news_base_url=news_base_url,
                            main_page_object=MainPage, news_page_object=NewsPage,
                            database_object=CollegeDB)

    def func_news_type(self, url):
        if 'stype=1' in url:
            return 1
        elif 'stype=2' in url:
            return 2
        elif 'stype=4' in url:
            return 4
        elif 'stype=6' in url:
            return 6
        elif 'stype=8' in url:
            return 8
        elif 'stype=9' in url:
            return 9
        elif 'stype=A' in url:
            return 10