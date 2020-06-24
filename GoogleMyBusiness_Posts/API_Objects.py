from typing import List
from enum import Enum



class Offer():
    def __init__(self, couponcode : str, redeemonlineurl : str, termsconditions : str,):
        self.couponCode = couponcode
        self.redeemOnlineUrl = redeemonlineurl
        self.termsConditions = termsconditions

class MediaFormat(Enum):
    MEDIA_FORMAT_UNSPECIFIED = "MEDIA_FORMAT_UNSPECIFIED"
    PHOTO = "PHOTO"
    VIDEO ="VIDEO"

class Media():
    def __init__(self, mediaformat : MediaFormat, sourceurl : str):
        self.mediaFormat = mediaformat
        self.sourceUrl = sourceurl

class StartDate():

    def __init__(self, year : int, month : int, day : int):
        self.year = year
        self.month = month
        self.day = day

class StartTime():
    
    def __init__(self, hours : int, minutes : int, seconds : int, nanos : int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.nanos = nanos

class EndDate():
    
    def __init__(self, year : int, month : int, day : int):
        self.year = year
        self.month = month
        self.day = day
    
class EndTime():
    def __init__(self, hours : int, minutes : int, seconds : int, nanos : int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.nanos = nanos

class Schedule():
    
    def __init__(self, startdate : StartDate, starttime : StartTime, enddate : EndDate, endtime : EndTime):
        self.startDate = startdate
        self.startTime = starttime
        self.endDate = enddate
        self.endTime = endtime

class Event():
    def __init__(self, title : str, schedule : Schedule):
        self.title = title
        self.schedule = schedule
  
class PostOffer():
    def __init__(self, media : List[Media], event : Event, summary : str, offer : Offer, topictype='OFFER', languagecode='en-US'):
        self.media = media
        self.event = event
        self.summary = summary
        self.offer = offer
        self.topicType = topictype
        self.languageCode = languagecode
