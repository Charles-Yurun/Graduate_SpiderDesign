# -*- coding: UTF-8 -*-
import threading

import leancloud
from gevent import monkey

from manager.college import CollegeManger
from manager.work import WorkManager


def register_leancloud():
    monkey.patch_all()
    leancloud.init(app_id='Xmh3GP4wHdgz4jPVpaW6jQYM-gzGzoHsz',
                   app_key='xBmSvfdpXxBkgDhjJuqqBIWW',
                   master_key='j8VdYDUkWaKGTirQQrKsFeUC')


def thread_factory(manager_object, base_url, thread_name):
    factory_manager = manager_object(base_url)
    factory_thread = threading.Thread(target=factory_manager.progress, name=thread_name)
    factory_thread.start()
    return factory_thread


def register_college_thread():
    thread_important_news = thread_factory(CollegeManger,'http://www.guet.edu.cn/ExtGuetWeb/News?stype=1',
                                           'important_news')
    thread_quick_message = thread_factory(CollegeManger, 'http://www.guet.edu.cn/ExtGuetWeb/News?stype=2',
                                          'quick_message')
    thread_notice_message = thread_factory(CollegeManger, 'http://www.guet.edu.cn/ExtGuetWeb/News?stype=4',
                                           'notice_message')
    thread_academic = thread_factory(CollegeManger, 'http://www.guet.edu.cn/ExtGuetWeb/News?stype=6',
                                     'academic_conference')
    thread_college = thread_factory(CollegeManger, 'http://www.guet.edu.cn/ExtGuetWeb/News?stype=8',
                                    'college_dynamics')
    thread_media = thread_factory(CollegeManger, 'http://www.guet.edu.cn/ExtGuetWeb/News?stype=9',
                                  'media_guet')
    thread_announcement = thread_factory(CollegeManger, 'http://www.guet.edu.cn/ExtGuetWeb/News?stype=A',
                                         'announcement')


def register_work_thread():
    thread_bulletin = thread_factory(WorkManager, 'http://job.myclub2.com/Home/ArticleList?label=03',
                                     'Employment_bulletin')
    thread_news = thread_factory(WorkManager, 'http://job.myclub2.com/Home/ArticleList?label=04',
                                 'Employment_name')
    thread_week = thread_factory(WorkManager, 'http://job.myclub2.com/Home/ArticleList?label=13',
                                 'week_company')
    thread_school = thread_factory(WorkManager, 'http://job.myclub2.com/Home/ArticleList?label=15',
                                   'shool_company')
    thread_network = thread_factory(WorkManager, 'http://job.myclub2.com/Home/ArticleList?label=16',
                                    'network_company')

if __name__ == '__main__':
    register_leancloud()

    # register_college_thread()

    register_work_thread()
    # thread_important_news.start()
    # thread_quick_message.start()
    # thread_notice_message.start()
    # thread_academic.start()
    # thread_college.start()
    # thread_media.start()
    # thread_announcement.start()

    # thread_important_news.join()
    # thread_quick_message.join()
    # thread_notice_message.join()
    # thread_academic.join()
    # thread_college.join()
    # thread_media.join()
    # thread_announcement.join()
