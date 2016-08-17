#tux_rss.py
#!/usr/bin/python
# -*- coding: utf-8 -*-
import feedparser
import tux_database
import tux_oop
from datetime import datetime, date, time
def getrssFeed(rssFeed):
 feed = feedparser.parse(rssFeed)
 if feed["bozo"] == 1:
   print "feed data isn't well-formed XML"
   print "RSS Fail"
   tux_database.Data("RF", str(datetime.now()))
 else:
   print "RSS Okay"
   tux_database.Data("RO", str(datetime.now()))
   title = feed['feed']['title']
 return title
