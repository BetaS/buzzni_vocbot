#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("/home/newmoni/workspace")

from utils.src.mail import Sender
from utils.src.crawler.CrawlUtil import CrawlUtil
from datetime import date

class GmailConnector(object):
    def __init__(self):
        account = ""
        passwd = ""

        fp = open("/home/newmoni/workspace/buzzni_vocbot/sender_account.secret", "r")
        account, passwd = fp.read().split(",")

        self.mail = Sender("gmail", account, passwd)

    def send(self, targets=[], content=""):
        """ type : pre, result
        """
        title = "%s 버즈니 VOC리포트" % (date.today())

        return self.mail.send(targets, title, content)

