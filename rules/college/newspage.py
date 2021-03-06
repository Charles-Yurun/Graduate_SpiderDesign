# -*- coding: UTF-8 -*-
import re
import datetime

from bs4 import BeautifulSoup, NavigableString, Tag
from HTMLParser import HTMLParseError


class NewsPage:

    def __init__(self, html_content):
        self.html_content = html_content
        self.soup_parser = BeautifulSoup(html_content, 'html5lib')

    def news_title(self):
        try:
            news_title = self.soup_parser.find('td', class_='newsTitle').string.strip()
        except:
            return None
        if news_title is None:
            print 'the news title is miss'
            return None
        return news_title

    def news_time(self):
        try:
            # news_time_tag = self.soup_parser.find('table').find_all('table')[1].find_all('td')[1].string
            news_time_tag = self.soup_parser.find('table').find('tbody')
            news_time_tag = unicode(news_time_tag)
        except HTMLParseError:
            return None
        pattern = re.compile(r'\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}')
        news_time = pattern.search(news_time_tag)
        if news_time:
            return news_time.group()
        else:
            print 'the news time is miss'
            return None

    def news_content(self):
        try:
            # news_content_tag = self.soup_parser.find('table').find_all('table')[1].find_all('td')[2].div.contents
            news_content_tag = self.soup_parser.find('table').find('tbody').find('tr').div.contents
            # print news_content_tag
        except:
            return 'the news content is miss '
        news_content = ''
        if not news_content_tag:
            print 'the news content is miss'
            return None
        for news in news_content_tag:
            if isinstance(news, NavigableString):
                news_content += news.string
            if isinstance(news, Tag):
                news_content += unicode(news)
        return news_content

    def news_all(self, news):
        news['news_title'] = self.news_title().encode('utf8')
        news['news_time'] = datetime.datetime.strptime(self.news_time().encode('utf8'), '%Y-%m-%d %H:%M')
        news['news_content'] = self.news_content().encode('utf8')
        return news
