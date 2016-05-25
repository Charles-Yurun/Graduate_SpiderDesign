# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup


class MainPage:

    def __init__(self, html_content):
        self.html_content = html_content
        self.soup_parser = BeautifulSoup(html_content, "html5lib")

    def find_news_next_page(self, base_url):
        try:
            next_page_href = self.soup_parser.find('div', class_='page_css page_line').find('span').find_all('a')[-2]
        except IndexError:
            print 'this is end file'
            return None
        if next_page_href is None:
            print 'next page url is not exist'
            return None
        else:
            next_page_url = next_page_href.get('href')
            if 'http' not in next_page_url:
                next_page_url = base_url + next_page_url
            return next_page_url

    def find_news_list(self, base_url):
        news_url_list = []
        try:

            origin_url_list = self.soup_parser.find('div', class_='article_list ').find('ul').find_all('li')
        except:
            print "list is miss"
            return None
        for news_url in origin_url_list:
            url = news_url.find('a').get('href')
            if 'http' not in url:
                url = base_url + url
                news_url_list.append(url)
        return news_url_list
