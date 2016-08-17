#module: tux_oop
# Author: Brian Tran
# Date: 06/11/2015
#purpose: entity module that contains the class tuxPayload members
import tux_regexp
import tux_database
class tuxPayload:
  def __init__(self, rssFeed, emailAddress, currentDate, costValue):
          self.rssFeed = rssFeed
          self.emailAddress = emailAddress
          self.currentDate = currentDate
          self.costValue = costValue
#Child class
class tuxPayloadFeed(tuxPayload):
  def __init__(self, rssFeed, emailAddress, currentDate, costValue):
      print "Feed : ", self.rssFeed, "Email : ", self.emailAddress, "Date : ", self.currentDate, "Cost : ", self.costValue
