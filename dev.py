# -*- coding: UTF-8 -*-
import threading

import leancloud
from gevent import monkey

from manager.college import CollegeManger
from manager.work import WorkManager
from manager.xsgzc import XsgzcManager

def register_leancloud():
    monkey.patch_all()
    leancloud.init(app_id='VcE8jVT2NvNdGuSnCtgt7Y5T-gzGzoHsz',
                   app_key='ReUMxlz8so3ewwijKuxSQRgb',
                   master_key='TzQXygjSfUUG49zQUeXe1U0n')


def thread_factory(manager_object, base_url, thread_name):
    factory_manager = manager_object(base_url)
    factory_thread = threading.Thread(target=factory_manager.progress, name=thread_name)
    factory_thread.start()
    return factory_thread


def register_college_thread():

    thread_important_news = thread_factory(CollegeManger, 'http://www.guet.edu.cn/ExtGuetWeb/News?stype=1&pageindex=245',
                                           'important_news')
    thread_quick_message = thread_factory(CollegeManger, 'http://www.guet.edu.cn/ExtGuetWeb/News?stype=2&&pageindex=291',
                                         'quick_message')
    thread_notice_message = thread_factory(CollegeManger, 'http://www.guet.edu.cn/ExtGuetWeb/News?stype=4&pageindex=146',
                                           'notice_message')
    thread_academic = thread_factory(CollegeManger, 'http://www.guet.edu.cn/ExtGuetWeb/News?stype=6&pageindex=29',
                                     'academic_conference')
    thread_college = thread_factory(CollegeManger, 'http://www.guet.edu.cn/ExtGuetWeb/News?stype=8&pageindex=62',
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


def register_xsgzc_thread():
    thread_wdmtg = thread_factory(XsgzcManager, 'http://xsgzc.guet.edu.cn/xwzx/wdmtg/', 'wdmtg')
    thread_wjhb = thread_factory(XsgzcManager, 'http://xsgzc.guet.edu.cn/xwzx/wjhb/', 'wjhb')
    thread_tzgg = thread_factory(XsgzcManager, 'http://xsgzc.guet.edu.cn/xwzx/tzgg/', 'tzgg')
    thread_xgdt = thread_factory(XsgzcManager, 'http://xsgzc.guet.edu.cn/xwzx/xgdt/', 'xgdt')

if __name__ == '__main__':
    register_leancloud()

    register_college_thread()

    register_work_thread()

    register_xsgzc_thread()
