from API_Objects import *


class GMB_Post():
    ADD_OFFER = 1
    ADD_EVENT = 2
    ADD_UPDATE = 3

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

    def test_create_post_oofer():
        post = create_post_offer(*start_end, Title='Title',CouponCode='',RedeemOnlineUrl='RedeemOnlineUrl', TermsConditions='TermsConditions',Summary='Summary',MediaList=[media1,media2])

def main():
    print('Running Main Function')
    

if __name__ == "__main__":
    main()