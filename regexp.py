#!/usr/bin/python
# -*- coding: utf-8 -*-
#module: tux_regexp
# Author :Brian Tran
# Date: 06 11 2015
# Purpose: accept user input and populate the tux entity and write the event status to the database.
import re
import tux_oop
import tux_database
from datetime import datetime, date, time
def UserInput():
 try:
#Validation for URL
  go = 1
  while go == 1:
   rssFeed = raw_input("Enter the RSS Feed: ")
   p = re.compile('^http\://[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3}(/\S*)?$')
   matchRssFeed = p.match(rssFeed)
   if matchRssFeed:
    print("rssFeed Accepted")
    go = 2
   else:
    print("Invalid rssFeed")
#Validation for Email
  while go == 2:
   emailAddress = raw_input("Enter the Email Address: ")
   p1 = re.compile('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$')
   checkEmailAddress = p1.match(emailAddress)
   if checkEmailAddress:
    print("Email entered Correctly")
    go = 3
   else:
    print("Email not entered Correctly")
#Validation for Date
  while go == 3:
   currentDate = raw_input("Enter the Date (YYYY-MM-DD): ")
   p2 = re.compile('^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$')
   checkCurrentDate = p2.match(currentDate)
   if checkCurrentDate:
    print("Date entered Correctly")
    go = 4
   else:
    print("Date entered incorrectly")
#Validation for Cost
  while go == 4:
   costValue = raw_input("enter the cost of service: ")
   p3 = re.compile('^\$?[0-9]+\.?[0-9]?[0-9]?$')
   checkCostValue = p3.match(costValue)
   if checkCostValue:
    print("Thank you for the dollar amount")
    go = 5
   else:
    print("Please only enter a dollar value")
    break
  if go == 5:
   print("rssFeed: " + rssFeed)
   print("Email: " + emailAddress)
   print("Current Date: " + currentDate)
   print("Cost Value: " + costValue)
  tuxPay = tux_oop.tuxPayload(rssFeed, emailAddress, currentDate, costValue)
  print "Input Okay"
  tux_database.Data("IO", str(datetime.now()))
  return tuxPay
 except Exception as e:
  print "Input Fail"
  tux_database.Data("IF", str(datetime.now()))
  print "Error : %s" % e.args[0]
