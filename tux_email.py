#!/usr/bin/python
# -*- coding: utf-8 -*-
#import smtplib for the actual sending function
import smtplib, tux_oop, tux_database, tux_rss
#Import the email modules we'll need
from email.mime.text import MIMEText
from datetime import datetime, date, time
#Setup the email components Subject, From, To
def emailAddress(emailAddress, currentDate):
 fromAddress = 'bkt5031@psu.edu'
 toAddress = emailAddress
 subject = 'RSS feed'
 try:
  f = open("rssFeed.html", "r")
  msg = MIMEText(f.read())
  msg["Subject"] = subject
  msg["From"] = fromAddress
  msg["To"] = toAddress
  f.close()
  s = smtplib.SMTP('smtp.psu.edu')
  s.sendmail(fromAddress, [toAddress], msg.as_string())
# Send the message via the SMTP server
  print "Email Okay"
  tux_database.Data("EO", str(datetime.now()))
 except Exception as e:
  print "Email Fail"
  tux_database.Data("EF", str(datetime.now()))
 finally:
  s.quit()
