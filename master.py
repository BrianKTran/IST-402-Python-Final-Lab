#!/usr/bin/python
# -*- coding: utf-8 -*-
#Module: tux_master
# Author: Brian Tran
# Date: 06112015
# Purpose: main running module that uses all the other modules
import tux_regexp, tux_database, tux_email
import tux_oop, tux_rss, subprocess
# Clear the screen
subprocess.call('clear', shell=True)
# Get the User Input:wq
tuxPay1 = tux_regexp.UserInput()
title = tux_rss.getrssFeed(tuxPay1.rssFeed)
emailAddress = tux_email.emailAddress(tuxPay1.emailAddress, tuxPay1.currentDate)
# Just to make sure it worked
print( "feed: " + tuxPay1.rssFeed)
print( "address: " + tuxPay1.emailAddress)
print( "date: " + tuxPay1.currentDate)
print( "cost: " + tuxPay1.costValue)
tux_rss.getrssFeed(tuxPay1.rssFeed)