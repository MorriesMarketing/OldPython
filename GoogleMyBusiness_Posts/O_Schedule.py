from typing import List
from enum import Enum
import jsons

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


def create_post_offer(*args, **kwargs):
    schedule = Schedule(
        startdate=StartDate(year=args[0], month=args[1], day=args[2]),
        starttime=StartTime(hours=args[3], minutes=args[4], seconds=args[5], nanos=args[6]),
        enddate=EndDate(year=args[7], month=args[8], day=args[9]),
        endtime=EndTime(hours=args[10], minutes=args[11], seconds=args[12], nanos=args[13])
        )

    event = Event(
        title=kwargs['Title'],
        schedule=schedule
        )

    offer = Offer(
        couponcode=kwargs['CouponCode'],
        redeemonlineurl=kwargs['RedeemOnlineUrl'],
        termsconditions=kwargs['TermsConditions']
        )

    #media = Media(
    #    mediaformat=MediaFormat.PHOTO,
    #    sourceurl=SourceUrl
    #    )

    postoffer = PostOffer(
        media=kwargs['MediaList'],
        event=event,
        summary=kwargs['Summary'],
        offer=offer
        )
    return postoffer

start = [1,1,1,2,2,2,2]
end = [3,3,3,4,4,4,4]
start_end = [*start, *end]
print(start_end)

media1 = Media(MediaFormat.PHOTO,sourceurl='url.jpg')
media2 = Media(MediaFormat.PHOTO,sourceurl='url2.jpg')
post = create_post_offer(*start_end, Title='Title',CouponCode='',RedeemOnlineUrl='RedeemOnlineUrl', TermsConditions='TermsConditions',Summary='Summary',MediaList=[media1,media2])

class IgnitePost():
    pass
class ClientPost():
    pass

post = jsons.dumps(post)

print(post)