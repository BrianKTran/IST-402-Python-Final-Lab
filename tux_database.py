
#!/usr/bin/python
# -*- coding: utf-8 -*-
# Module:tux_database
# Author: Brian Tran
# Date: 06 11 2015
# Purpose: contains the functions that will hanlde the tux event status CRUD
import sqlite3 as lite
import sys

from datetime import datetime, date, time

try:
 con = lite.connect('tux.db')
 with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF exists EventLookin")
    cur.execute("DROP TABLE IF exists EventStatus")
    cur.execute("CREATE TABLE EventLookin(EventID TEXT PRIMARY KEY, EventType TEXT, EventDate)")
    cur.execute("CREATE TABLE EventStatus(EventID INTEGER PRIMARY KEY, EventType TEXT, EventDate, FOREIGN KEY(EventType) REFERENCES Lookin(EventType) )")
    cur.execute("INSERT INTO EventLookin VALUES('RO:',' RSS Okay  ',' Date: ' )")
    cur.execute("INSERT INTO EventLookin VALUES('RF:',' RSS Fail  ',' Date: ' )")
    cur.execute("INSERT INTO EventLookin VALUES('EO:',' Email Okay',' Date: ' )")
    cur.execute("INSERT INTO EventLookin VALUES('EF:',' Email Fail',' Date: ' )")
    cur.execute("INSERT INTO EventLookin VALUES('IO:',' Input Okay',' Date: ' )")
    cur.execute("INSERT INTO EventLookin VALUES('IF:',' Input Fail',' Date: ' )")
    con.commit()
except lite.Error, e:
 if con:
  con.rollback()
  print"Error %s: " % e.args[0]
  sys.exit(1)

finally:
 if con:
  con.close()

def Data(EventType, EventDate):
 try:
  con = lite.connect("tux.db")
  with con:
   cur = con.cursor()

   insertstring = "INSERT INTO EventStatus Values (NULL,'"  + EventType + "','" + EventDate + "')"
   cur.execute(insertstring)

 finally:
  if con:
   con.close()
