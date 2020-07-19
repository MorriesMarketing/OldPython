import dominate
from dominate.tags import *
from dominate.util import raw

class SpecialsPagev1():
    def __init__(self,vehicles,d):
        self.specialspage = dominate.document(title=f'{d.DealerName} Lease & Finance Specials')
        self.vehicles = vehicles
        self.dealer = d
        
    def advertised_offer(v,o):
        if o.OfferTypeID == 1 or o.OfferTypeID == 3 or o.OfferTypeID == 4 or o.OfferTypeID == 6:
            with div(id=f"{v.YearMakeModelurl}-{o.OfferTypeurl}-Lease-Special-Advertised-Offer", cls="d-flex justify-content-center advertised-lease-offer"):
                div(f"{o.Payment}", cls="payment")
                div("/Mo.", cls="month")
        elif o.OfferTypeID == 5:
            with div(id=f"{v.YearMakeModelurl}-{o.OfferTypeurl}-Lease-Special-Advertised-Offer", cls="d-flex flex-column advertised-lease-offer"):
                div(f"{o.DueAtSigning}", cls="one-pay-due-at-signing")
                div("Due at Signing", cls="one-pay-text")
        elif o.OfferTypeID == 7:
            with div(id=f"{v.YearMakeModelurl}-{o.OfferTypeurl}-Lease-Special-Advertised-Offer", cls="d-flex justify-content-center advertised-lease-offer"):
                if o.APR == 0.0:
                    div(f"0", cls="apr")
                else:
                    div(f"{o.APR}", cls="apr")
                div("% APR", cls="month")
        

    def offer_details(v,o):
        if o.OfferTypeID == 1 or o.OfferTypeID == 3 or o.OfferTypeID == 4 or o.OfferTypeID == 5:
            with div (id="term-mileage", cls="d-flex justify-content-center"):
                with div(id=f"{v.YearMakeModelurl}-{o.OfferTypeurl}-Lease-Special-Term", cls="d-flex justify-content-center"):
                    div(f"{o.Term}", cls="term", style="margin: 0px 5px 0px 0px;")
                    div("Month Lease", cls="term")
                div ("|", style="margin: 0px 5px 0px 5px;")
                with div(id=f"{v.YearMakeModelurl}-{o.OfferTypeurl}-Lease-Special-Mileage", cls="d-flex justify-content-center"):
                    div (f"{o.Mileage}", cls="mileage", style="margin: 0px 5px 0px 0px;")
                    div ("Miles/Yr.", cls="mileage")
        elif o.OfferTypeID == 6:
            with div (id="term-mileage", cls="d-flex justify-content-center"):
                with div(id=f"{v.YearMakeModelurl}-{o.OfferTypeurl}-Special-Term", cls="d-flex justify-content-center"):
                    div(f"{o.Term}", cls="term", style="margin: 0px 5px 0px 0px;")
                    div("Months Financed", cls="term")
        elif o.OfferTypeID == 7:
            with div (id="term-mileage", cls="d-flex justify-content-center"):
                with div(id=f"{v.YearMakeModelurl}-{o.OfferTypeurl}-Special-Term", cls="d-flex justify-content-center"):
                    div(f"{o.Term}", cls="term", style="margin: 0px 5px 0px 0px;")
                    div("Months Financed", cls="term")

        if o.OfferTypeID == 5:
            with div (id="payment-down", cls="d-flex justify-content-center"):
                with div (id="", cls="d-flex justify-content-center"):
                    div (f"{o.Payment}", cls="one-pay-payment", style="margin: 0px 5px 0px 0px;")
                    div ("/Mo.", cls="one-pay-payment")
                div ("|", style="margin: 0px 5px 0px 5px;")
                with div (id=f"{v.YearMakeModelurl}-{o.OfferTypeurl}-Lease-Special-Down-Payment", cls="d-flex justify-content-center"):
                    div (f"{o.DownPayment}", cls="down-payment", style="margin: 0px 5px 0px 0px;")
                    div ("Down Payment", cls="down-payment")
        elif o.OfferTypeID == 1 or o.OfferTypeID == 3 or o.OfferTypeID == 4 or o.OfferTypeID == 5 or o.OfferTypeID == 6:
            with div (id="down-due-at-signing", cls="d-flex justify-content-center"):
                with div (id=f"{v.YearMakeModelurl}-{o.OfferTypeurl}-Lease-Special-Down-Payment", cls="d-flex justify-content-center"):
                    div (f"{o.DownPayment}", cls="down-payment", style="margin: 0px 5px 0px 0px;")
                    div ("Down Payment", cls="down-payment")
                div ("|", style="margin: 0px 5px 0px 5px;")
                with div (id=f"{v.YearMakeModelurl}-{o.OfferTypeurl}-Lease-Special-Due-at-Signing", cls="d-flex justify-content-center"):
                    div (f"{o.DueAtSigning}", cls="due-at-signing", style="margin: 0px 5px 0px 0px;")
                    div ("Due at Signing", cls="due-at-signing")
        #{v.YearMakeModelurl}-{o.OfferTypeurl}-Special
    def special(v):
        #This begins the Offer Section of HTML
        for o in v.Offers:
            show = ''
            if o.OfferTypeID == 3 or o.OfferTypeID == 6:
                show = 'collapse show'
            else:
                show = 'collapse'

            with div(id= f"offertype{o.OfferTypeID}" , cls=show):
                with div (id= f"{v.YearMakeModelurl}-{o.OfferTypeurl}-Special" , cls=f" d-flex flex-column"):
                    with div (id=f"{v.YearMakeModelurl}-{o.OfferTypeurl}-Special-Title"):
                        if o.OfferTypeID == 1 or o.OfferTypeID == 3 or o.OfferTypeID == 4 or o.OfferTypeID == 5:
                            special = f"{o.OfferType} Lease Special*"
                        if o.OfferTypeID == 6 :
                            special = f"Low Payment Finance Special*"
                        if o.OfferTypeID == 6 :
                            special = f"Low APR Finance Special*"
                        a (special, cls="offer-type", href=f"#Disclaimer-{v.YearMakeModelurl}-{o.OfferTypeID}", data_toggle="collapse")
                        
                    SpecialsPagev1.advertised_offer(v,o)
                    SpecialsPagev1.offer_details(v,o)
            
                    with div (id=f"Disclaimer-{v.YearMakeModelurl}-{o.OfferTypeID}", cls="collapse"):
                        hr()
                        p(f"{o.Disclaimer}", cls="disclaimer")
                    hr()

    def vehicle_html(v):
        
        #This begins the Vehicle Section of the HTML
        with div(cls=f"vehicle year{v.Year} collapse show",id=f"{v.YearMakeModelurl}-Lease-and-Finance-Specials"):
            with div(style="width:100%;height:220px;"):
                with a(href=f"{v.Image.UrlVdp}",style="margin: 1px 0px 0px 0px"):
                    img(id=f"{v.YearMakeModelTrimurl}-image", src=f"{v.Image.PhotoURL}", alt=f"{v.YearMakeModelTrim}", style="float:left;width:100%;height:100%;object-fit:cover;")
            div(f"{v.YearMakeModelTrim}", cls="vehicle-title" )
            br()
            br()
            SpecialsPagev1.special(v)
            with div(cls='buttonz'):
                with a(href=f"{v.Image.UrlVdp}"):
                    button("View Vehicle",type="button" ,cls="btn btn-primary", style="margin: 0px 0px 0px 0px")
                with a(href=f"{v.InventoryUrl}"):
                    button("View Inventory",type="button" ,cls="btn btn-primary", style="margin: 0px 0px 0px 0px")
                with a(href="#form"):
                    button("Claim Offer",type="button" ,cls="btn btn-primary", style="margin: 5px 0px 0px 0px")

    def doc(self):
        with self.specialspage.head:
            meta (name="viewport", content="width=device-width, initial-scale=1")
            link (rel="stylesheet", href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css")
            script (src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js")
            script (src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js")
            script (src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js")
            raw("""<script>
                    $(document).ready(function(){
                      $("#hide").click(function(){
                        $("p").hide();
                      });
                      $("#show").click(function(){
                        $("p").show();
                      });
                    });
                    </script>
                           """)

            style("""
            .container{
            max-width: 1500px;
            }
            .flex-container {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
  
            }
            .btn-group {
            margin: 5px 0px 5px 0px;
            padding: 5px;
            }
            hr {
	            border: .5px solid #C3C3C3;
	            margin: 10px 20px;
            }
            .filterbox{
            background-color: #f1f1f1;
            }
            .vehicle {
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
            font-size: 15px;
            font-weight: 700;
            margin: 5px 0px 0px 0px;
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
            .filterbutton {
            width: 100px;
            text-align: left;
            margin: 5px 0px 0px 0px;
            }
            """, is_pretty = True)
            
        with self.specialspage:
            with div(cls="container"):
                with div(cls="row"):
                    with div( cls="col-sm-2 filterbox", style="padding: 15px"):
                        with div (id='filters', cls="btn-group-vertical"):
                            with div():
                                button ("Lease", type="button" ,cls="btn btn-secondary filterbutton", data_target=".leasefilter", data_toggle="collapse")
                                with div (cls="leasefilter collapse"):
                                    with div (cls="checkbox"):
                                        raw("""<label><input type="checkbox" data-target="#offertype3" data-toggle="collapse" checked> 10% MSRP Down</label>""")
                                    with div (cls="checkbox"):
                                        raw("""<label><input type="checkbox" data-target="#offertype1" data-toggle="collapse"> $0 Down Payment</label>""")
                                    with div (cls="checkbox"):
                                        raw("""<label><input type="checkbox" data-target="#offertype4" data-toggle="collapse"> Sign & Drive</label>""")
                                    with div (cls="checkbox"):
                                        raw("""<label><input type="checkbox" data-target="#offertype5" data-toggle="collapse"> One Pay</label>""")
                            with div():
                                button ("Finance", type="button" ,cls="btn btn-secondary filterbutton", data_target=".financefilter", data_toggle="collapse")
                                with div ( cls="financefilter collapse" ):
                                    with div (cls="checkbox"):
                                        raw("""<label><input type="checkbox" data-target="#offertype6" data-toggle="collapse" checked> Low Finance Payment</label>""")
                                    with div (cls="checkbox"):
                                        raw("""<label><input type="checkbox" data-target="#offertype7" data-toggle="collapse"> Low Finance APR</label>""")
                            with div():
                                button ("Year", type="button" ,cls="btn btn-secondary filterbutton", data_target=".yearfilter", data_toggle="collapse")
                                with div ( cls="yearfilter collapse" ):
                                    with div (cls="checkbox"):
                                        raw("""<label><input type="checkbox" data-target=".year2019" data-toggle="collapse" checked> 2019</label>""")
                                    with div (cls="checkbox"):
                                        raw("""<label><input type="checkbox" data-target=".year2020" data-toggle="collapse" checked> 2020</label>""")
                    with div(cls="flex-container col-sm-10"):
                    
                        for v in self.vehicles:
                            if self.dealer.Domain == 'https://www.walserautocampus.com/':
                                if v.State == 'KS':
                                    SpecialsPagev1.vehicle_html(v)

                            else:
                                SpecialsPagev1.vehicle_html(v)
            

        return self.specialspage

    
#text = SpecialsPagev1()

#print(text.doc())
    
    

    
