#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#__author__ = 'eltsai'
from datetime import datetime
import schedule
import time
import os

log_prefix = 'logs/log-'
day = datetime.today().strftime('%Y-%m-%d')
def job():
    os.system('./playlist-bot.py -log '+log_prefix+day+'.txt')
    schedule.every().day.at("00:00").do(job)

os.system('./playlist-bot.py -log '+log_prefix+day+'.txt')
while True:
    schedule.run_pending()
    time.sleep(1)