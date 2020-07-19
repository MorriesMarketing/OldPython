
import dominate
from dominate.tags import *

class SpecialsPagev1():
    def __init__(self,vehicles):
        self.specialspage = dominate.document(title='Dominate your HTML')
        self.vehicles = vehicles
        
    
    def doc(self):
        with self.specialspage.head:
            meta (name="viewport", content="width=device-width, initial-scale=1")
            link (rel="stylesheet", href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css")
            script (src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js")
            script (src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js")
            script (src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js")
            style("""
            .flex-container {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
  
            }
            hr {
	            border: .5px solid #C3C3C3;
	            margin: 10px 20px;
            }
            .flex-container > div {
                background-color: #f1f1f1;
                width: 325px;
                margin: 10px;
                text-align: center;
                line-height: 20px;
                font-size: 15px;
                justify-content: center;
            }
            .disclaimer {
            font-size: 10px;
            margin: 0px 5px 0px 5px;
            }
            .payment {
            font-size: 35px;
            font-weight: 700;
            margin: 15px 0px;
            }
            .one-pay-payment {
            font-size: 12px;
            }
            .one-pay-due-at-signing {
            font-size: 30px;
            font-weight: 700;
            margin: 15px 0px 0px 0px;
            }
            .apr {
            font-size: 30px;
            font-weight: 700;
            margin: 15px 0px;
            }
            .offer-type {
            font-size: 15px;
            font-weight: 600;
            }
            .month {
            font-size: 20px;
            font-weight: 700;
            margin: 20px 0px;
            }
            .one-pay-text {
            font-size: 20px;
            }
            .term {
            font-size: 12px;
            }
            .down-payment {
            font-size: 12px;
            }
            .due-at-signing {
            font-size: 12px;
            }
            .mileage {
            font-size: 12px;
            }
            .vehicle-title {
            font-size: 20px;
            margin: 15px 2px 0px 2px;
            font-weight: 700;
            height: 40px
            }
            .buttonz {

            margin: 15px 0px 15px 0px;

            }
            """)
        
        with self.specialspage:
            with div(cls="container"):
                with div(cls="flex-container"):
                    for v in self.vehicles:
                        #This begins the Vehicle Section of the HTML
                        with div(id=f"{v.YearMakeModelurl}-Lease-and-Finance-Specials"):
                            with div(style="width:100%;height:200px;"):
                                with a(href=f"{v.Image.UrlVdp}"):
                                    img(id=f"{v.YearMakeModelTrimurl}-image", src=f"{v.Image.UrlVdp}", alt=f"{v.YearMakeModelTrim}", style="float:left;width:100%;height:100%;object-fit:cover;")
                            div(f"{v.YearMakeModelTrim}", cls="vehicle-title" )
                            br()
                            br()
                            for o in v.Offers:
                                with div (id= f"{v.YearMakeModelurl}-{o.OfferTypeurl}-Special" , cls="d-flex flex-column"):
                                    with div (id=f"{v.YearMakeModelurl}-{o.OfferTypeurl}-Special-Title"):
                                        a (f"{o.OfferType}", cls="offer-type collapsed", href=f"#{v.YearMakeModelurl}-{o.OfferTypeurl}-Disclaimer", data_toggle="collapse")
                        
                                    if o.OfferTypeID == 1 or o.OfferTypeID == 3 or o.OfferTypeID == 4 or o.OfferTypeID == 6:
                                        with div(id=f"{v.YearMakeModelurl}-{o.OfferTypeurl}-Lease-Special-Advertised-Offer", cls="d-flex justify-content-center advertised-lease-offer"):
                                            div(f"{o.Payment}", cls="payment")
                                            div("/Mo.", cls="month")
                                    elif o.OfferTypeID == 5:
                                        with div(id=f"{v.YearMakeModelurl}-{o.OfferTypeurl}-Lease-Special-Advertised-Offer", cls="d-flex justify-content-center advertised-lease-offer"):
                                            div(f"{o.DueAtSigning}", cls="one-pay-due-at-signing")
                                            div("Due at Signing", cls="one-pay-text")
                                    elif o.OfferTypeID == 7:
                                        with div(id=f"{v.YearMakeModelurl}-{o.OfferTypeurl}-Lease-Special-Advertised-Offer", cls="d-flex justify-content-center advertised-lease-offer"):
                                            div(f"{o.APR}", cls="apr")
                                            div("% APR", cls="month")

                                    if o.OfferTypeID == 1 or o.OfferTypeID == 3 or o.OfferTypeID == 4 or o.OfferTypeID == 5 or o.OfferTypeID == 6:
                                        with div (id="term-mileage", cls="d-flex justify-content-center"):
                                            with div(id=f"{v.YearMakeModelurl}-{o.OfferTypeurl}-Lease-Special-Term", cls="d-flex justify-content-center"):
                                                div(f"{o.Term}", cls="term", style="margin: 0px 5px 0px 0px;")
                                                div("Month Lease", cls="term")
                                            div ("|", style="margin: 0px 5px 0px 5px;")
                                            with div(id=f"{v.YearMakeModelurl}-{o.OfferTypeurl}-Lease-Special-Mileage", cls="d-flex justify-content-center"):
                                                div (f"{o.Mileage}", cls="mileage", style="margin: 0px 5px 0px 0px;")
                                                div ("Miles/Yr.", cls="mileage")
                                    elif o.OfferTypeID == 7:
                                        with div (id="term-mileage", cls="d-flex justify-content-center"):
                                            with div(id=f"{v.YearMakeModelurl}-{o.OfferTypeurl}-Special-Term", cls="d-flex justify-content-center"):
                                                div(f"{o.Term}", cls="term", style="margin: 0px 5px 0px 0px;")
                                                div("Months Financed", cls="term")

                                    if o.OfferTypeID == 5:
                                        with div (id="payment-down", cls="d-flex justify-content-center"):
                                            with div (id="", cls="d-flex justify-content-center"):
                                                div (f"{o.Payment}", cls="one-pay-payment", style="margin: 0px 5px 0px 0px;")
                                                div ("/Mo.", cls="")
                                            div ("|", style="margin: 0px 5px 0px 5px;")
                                            with div (id=f"{v.YearMakeModelurl}-{o.OfferTypeurl}-Lease-Special-Down-Payment", cls="d-flex justify-content-center"):
                                                div (f"{o.DownPayment}", cls="down-payment", style="margin: 0px 5px 0px 0px;")
                                                div ("Down Payment", cls="down-payment")
                                    elif o.OfferTypeID == 1 or o.OfferTypeID == 3 or o.OfferTypeID == 4 or o.OfferTypeID == 5 or o.OfferTypeID == 6:
                                        with div (id="down-due-at-signing", cls="d-flex justify-content-center"):
                                            with div (id="f{v.YearMakeModelurl}-{o.OfferTypeurl}-Lease-Special-Down-Payment", cls="d-flex justify-content-center"):
                                                div (f"{o.DownPayment}", cls="down-payment", style="margin: 0px 5px 0px 0px;")
                                                div ("Down Payment", cls="down-payment")
                                            div ("|", style="margin: 0px 5px 0px 5px;")
                                            with div (id=f"{v.YearMakeModelurl}-{o.OfferTypeurl}-Lease-Special-Due-at-Signing", cls="d-flex justify-content-center"):
                                                div (f"{o.DueAtSigning}", cls="due-at-signing", style="margin: 0px 5px 0px 0px;")
                                                div ("Due at Signing", cls="due-at-signing")

                                    
            
                                    with div (id=f"{v.YearMakeModelurl}-{o.OfferTypeurl}-Disclaimer", cls="collapse"):
                                        hr()
                                        p(f"{o.Disclaimer}", cls="disclaimer")
                                    hr()

        return self.specialspage

    
#text = SpecialsPagev1()

#print(text.doc())
    
    

    
