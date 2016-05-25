# coding: UTF-8
import re
import datetime

from bs4 import BeautifulSoup, Tag
from HTMLParser import HTMLParseError


class NewsPage:

    def __init__(self, html_content):
        self.html_content = html_content
        self.soup_parser = BeautifulSoup(html_content, 'html5lib')

    def news_title(self):
        try:
            news_title = self.soup_parser.find('div', class_='main05').find('table').\
                find('tbody').find_all_next('tr')[0].find('h2').string.strip()
        except IndexError:
            print 'the news title is miss'
            return None
        if news_title is None:
            print 'the news title is miss'
            return None
        else:
            return news_title

    def news_time(self):
        try:
            news_time_tag = self.soup_parser.find('div', class_='main05').find('table').\
                find('tbody').find_all_next('tr')[1]
        except IndexError:
            print 'the news title is miss'
            return None
        pattern = re.compile(r'\d{4}/\d{1,2}/\d{1,2} \d{1,2}:\d{1,2}')
        news_time_tag = unicode(news_time_tag)
        news_time = pattern.search(news_time_tag)
        if news_time:
            return news_time.group()
        else:
            print 'the news time is miss'
            return None

    def news_content(self):
        try:
            news_content = self.soup_parser.find('div', class_='main05').find('table').\
                find('tbody').find_all_next('tr')[2]
        except HTMLParseError and IndexError:
            print 'the news content is miss'
            return None
        if not news_content:
            print 'the news content is miss'
            return None
        if isinstance(news_content, Tag):
            news_content = unicode(news_content)
        return news_content

    def news_all(self, news):
        news['news_title'] = self.news_title().encode('utf8')
        news['news_time'] =datetime.datetime.strptime(self.news_time().encode('utf8'), "%Y/%m/%d %H:%M")
        news['news_content'] =self.news_content().encode('utf8')
        return news