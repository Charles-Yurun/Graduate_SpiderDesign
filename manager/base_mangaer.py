# -*- coding: UTF-8 -*-
import threading
import time

from spider.spider import Spider


class BaseManger:

    def __init__(self, base_url, news_base_url, main_page_object, news_page_object, database_object):
        self.base_url = base_url
        self.news_base_url = news_base_url
        self.news_type = self.func_news_type(news_base_url)
        self.main_page_object = main_page_object
        self.news_page_object = news_page_object
        self.database_object = database_object

    def func_news_type(self, url):
        print 'baseManger'
        pass

    def news_content(self, url):
        x = Spider(url)
        print "------------------------------------"
        print url, self.news_type
        news_content_page = self.news_page_object(x.get_page())
        news = {}
        news = news_content_page.news_all(news)
        news['news_url'] = url.encode('utf8')
        news['news_type'] = self.news_type
        if self.database_object.is_existed(url):
            print 'this url is existed'
            return False
        else:
            database = self.database_object(**news)
            database.save()
        return True

    def news_content_by_list(self, news_list):
        for url in news_list:
            if not self.news_content(url):
                return False
        return True

    def progress(self):
        while True:
            news_next_url = self.news_base_url
            while news_next_url:
                print news_next_url
                if news_next_url is not None:
                    x = Spider(news_next_url)
                    news_list_source = self.main_page_object(x.get_page())
                    news_list = news_list_source.find_news_list(self.base_url)
                    if not self.news_content_by_list(news_list):
                        break
                    news_next_url = news_list_source.find_news_next_page(self.base_url)
                    time.sleep(5)
                else:
                    break
            print 'sleep 300s current_thread name is %s' % threading.current_thread().getName()
            time.sleep(300)
