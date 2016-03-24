# -*- coding: UTF-8 -*-

import time
import socket
import urllib2


class Spider:

    def __init__(self, base_url):
        self.base_url = base_url

    def get_page(self):
        global response
        try:
            response = urllib2.urlopen(self.base_url)
        except urllib2.URLError:
            print "url is not exist"
        except socket.timeout:
            print 'socket timeout'
            time.sleep(30)
            self.get_page()

        html = response.read()
        return html
