#!/usr/bin/env python
# -*- coding: utf-8 -*-

from GmailConnector import GmailConnector
from utils.src.DbMgr import DbMgr
import utils.src.timeutil as timeutil
import random, imaplib, datetime, time

def load_db():
    fp = open("/home/newmoni/workspace/buzzni_vocbot/db_account.secret", "r")
    account, passwd, server, db, tbl = fp.read().split(",")
    return DbMgr(account, passwd, server, db, tbl, 3)

def app_review(appcode):
    content = ""
    search_date = int(timeutil.change_fmt(datetime.date.today()-datetime.timedelta(days=1), "%Y-%m-%d", "%Y%m%d"))
    content += "\t\t\t\t기준일: "+str(search_date)+"\n"

    result = DB.select(["title", "author", "content", "score", "version"], {"entity_id": appcode, "date":search_date})

    content += "\t\t\t\t리뷰수: "+str(len(result))+"\n\n\n"

    for review in result:
        content += review[1]+": "+review[0]+" (평가: "+str(review[3])+", 버전: "+str(review[4])+")"+"\n"
        for data in review[2].split("\n"):
            content += "\t"+data+"\n"
        content += "\n"
    return content

if __name__ == "__main__":
    DB = load_db()

    content = """
         Voice of Customer Report
    ================================
                            (by. Eric)\n\n\n\n"""

    content += """
    ## 버즈니 영화 가이드(for iOS)\n"""
    content += app_review(588868)

    content += """\n
    ## 버즈니 맛집 가이드(for iOS)\n"""
    content += app_review(936334)

    content += """\n
    ## 버즈니 지하철맛집(for iOS)\n"""
    content += app_review(936801)

    a = GmailConnector()

    a.send(["team@buzzni.com"], content)















