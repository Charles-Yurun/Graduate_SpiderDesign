# -*- coding: UTF-8 -*-
from base_mangaer import BaseManger
from database.Xsgzc import XsgzcDB
from rules.xsgzc import MainPage
from rules.xsgzc import NewsPage


class XsgzcManager(BaseManger):

    def __init__(self, news_base_url):
        BaseManger.__init__(self, base_url='http://xsgzc.guet.edu.cn/', news_base_url=news_base_url,
                            main_page_object=MainPage, news_page_object=NewsPage,
                            database_object=XsgzcDB)

    def func_news_type(self, url):
        if 'wdmtg' in url:
            return 1
        elif 'wjhb' in url:
            return 2
        elif 'gjzxdk' in url:
            return 3
        elif 'xsgzjb' in url:
            return 4
        elif 'tzgg' in url:
            return 5
        elif 'xyfc' in url:
            return 6
        elif 'xgdt' in url:
            return 7
