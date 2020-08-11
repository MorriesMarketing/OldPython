import dominate
from dominate.tags import *
from dominate.util import raw

class SpecialsPagev1():
    def __init__(self,vehicles,d,Years,Models,Makes):
        self.specialspage = dominate.document(title=f'{d.DealerName} Lease & Finance Specials')
        self.vehicles = vehicles
        self.dealer = d
        self.years = Years
        self.models = Models
        self.makes = Makes
        
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
    def special(self,v):
        #This begins the Offer Section of HTML
        for o in v.Offers:
            if str(o.OfferTypeID) in self.dealer.OfferTypeIDsActive:
                show = ''
                if o.OfferTypeID == 3 or o.OfferTypeID == 6:
                    show = 'collapse show'
                else:
                    show = 'collapse'

                with div(id= f"offertype{o.OfferTypeID}" , cls=f'cell offertype{o.OfferTypeID}'):
                    with div (id= f"{v.YearMakeModelurl}-{o.OfferTypeurl}-Special" , cls=f" d-flex flex-column"):
                        with div (id=f"{v.YearMakeModelurl}-{o.OfferTypeurl}-Special-Title"):
                            if o.OfferTypeID == 1 or o.OfferTypeID == 3 or o.OfferTypeID == 4 or o.OfferTypeID == 5:
                                special = f"{o.OfferType} Lease Special*"
                            if o.OfferTypeID == 6 :
                                special = f"Low Payment Finance Special*"
                            if o.OfferTypeID == 6 :
                                special = f"Low APR Finance Special*"
                            a (special, cls="offer-type", href=f"#Disclaimer-{v.VIN}-{o.OfferTypeID}", data_toggle="collapse")
                        
                        SpecialsPagev1.advertised_offer(v,o)
                        SpecialsPagev1.offer_details(v,o)
            
                        with div (id=f"Disclaimer-{v.VIN}-{o.OfferTypeID}", cls="collapse"):
                            hr()
                            p(f"{o.Disclaimer}", cls="disclaimer")
                        hr()

    def vehicle_html(self,v):
        
        #This begins the Vehicle Section of the HTML
        with div(cls=f"vehicle cell year{v.Year} {v.MakeName} {v.Modelurl}",id=f"{v.YearMakeModelurl}-Lease-and-Finance-Specials"):
            with div(style="width:100%;height:220px;"):
                with a(href=f"{v.Image.UrlVdp}",style="margin: 1px 0px 0px 0px"):
                    img(id=f"{v.YearMakeModelTrimurl}-image", src=f"{v.Image.PhotoURL}", alt=f"{v.YearMakeModelTrim}", style="float:left;width:100%;height:100%;object-fit:cover;")
            div(f"{v.YearMakeModelTrim}", cls="vehicle-title" )
            br()
            br()
            SpecialsPagev1.special(self,v)
            with div(cls='buttonz'):
                with a(href=f"{v.Image.UrlVdp}"):
                    button("View Vehicle",type="button" ,cls="btn btn-primary", style="margin: 0px 0px 0px 0px")
                website = f'{self.dealer.Domain}{self.dealer.NewVehicleSearch}'
                with a(href=f"{website}{v.Inventory}"):
                    button("View Inventory",type="button" ,cls="btn btn-primary", style="margin: 0px 0px 0px 0px")
                with a(href="#form"):
                    button("Claim Offer",type="button" ,cls="btn btn-primary", style="margin: 5px 0px 0px 0px")
    
    def checkbox(type,checked,description):
        with div ():
            raw(f"""<label><input type="checkbox" class="checkbox" value="offertype{type}" {checked}> {description}</label>""")

    def chooseOfferTypes(self,button):
        for type in self.dealer.OfferTypeIDsActive:
            checked = ''
            description = ''
            dealtype = ''
            if type in self.dealer.OfferTypesOnLoad:
                checked = 'checked'
            for ot in self.dealer.OfferTypes:
                if int(ot.OfferTypeID) == int(type):
                    description = ot.Description  
                    dealtype = ot.DealType
            if button == dealtype:
                SpecialsPagev1.checkbox(type,checked,description)

    def doc(self):
        with self.specialspage.head:
            meta (name="viewport", content="width=device-width, initial-scale=1")
            link (rel="stylesheet", href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css")
            script (src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js")
            script (src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js")
            script (src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js")
            raw("""<script>
	            window.onload = function() {
		            var checkboxes = document.getElementsByClassName("checkbox");
		
		            for (var i = 0; i < checkboxes.length; i++) {
			            checkboxes[i].addEventListener("change", toggleCells);
		            }
		
		            toggleCells();
	            }

	            function toggleCells() {
		            var checkboxes = document.getElementsByClassName("checkbox");
		            var cells = document.getElementsByClassName("cell");
		
		            for (var i = 0; i < checkboxes.length; i++) {
			            for (var j = 0; j < cells.length; j++) {
				            var value = checkboxes[i].value;
				
				            if (cells[j].classList.contains(value)) {
					            if (checkboxes[i].checked == true) {
						            cells[j].style.display = "";
					            }
					            else {
						            cells[j].style.display = "none";
					            }
				            }
			            }
		            }
	            }
            </script>
            <script>
            $(document).ready(function(){
              $("#myInput").on("keyup", function() {
                var value = $(this).val().toLowerCase();
                $(".modelfilter div").filter(function() {
                  $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
                });
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
                                    SpecialsPagev1.chooseOfferTypes(self,button="Lease")
                                    
                            with div():
                                button ("Finance", type="button" ,cls="btn btn-secondary filterbutton", data_target=".financefilter", data_toggle="collapse")
                                with div ( cls="financefilter collapse" ):
                                    SpecialsPagev1.chooseOfferTypes(self,button="Finance")

                            with div():
                                button ("Year", type="button" ,cls="btn btn-secondary filterbutton", data_target=".yearfilter", data_toggle="collapse")
                                with div ( cls="yearfilter collapse" ):
                                    for y in self.years:
                                        with div ():
                                            raw(f"""<label><input type="checkbox" class="checkbox" value="year{y}" checked> {y}</label>""")
                            with div():
                                button ("Makes", type="button" ,cls="btn btn-secondary filterbutton", data_target=".makefilter", data_toggle="collapse")
                                with div ( cls="makefilter collapse" ):
                                    for m in self.makes:
                                        with div ():
                                            raw(f"""<label><input type="checkbox" class="checkbox" value="{m}" checked> {m}</label>""")
                            with div():
                                button ("Models", type="button" ,cls="btn btn-secondary filterbutton", data_target=".modelfilter", data_toggle="collapse")

                                with div ( cls="modelfilter collapse" ):
                                    #raw("""<label><input class="form-control" id="myInput" type="text" placeholder="Search.."></label>""")
                                    for m in self.models:
                                        with div ():
                                            raw(f"""<label><input type="checkbox" class="checkbox" value="{m[1]}" checked> {m[0]}</label>""")
                    with div(cls="flex-container col-sm-10"):
                    
                        for v in self.vehicles:
                            if v.Image.PhotoURL != None and v.Image.UrlVdp != None:
                                if self.dealer.Domain == 'https://www.walserautocampus.com/':
                                    if v.State == 'KS':
                                        SpecialsPagev1.vehicle_html(self,v)

                                else:
                                    SpecialsPagev1.vehicle_html(self,v)
            

        return self.specialspage

    
#text = SpecialsPagev1()

#print(text.doc())
    
    

    
