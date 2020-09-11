import dominate
from dominate.tags import *
from dominate.util import raw
from O_Days import *

class Dashboard():
    def __init__(self,clients):
        self.Dashboard = dominate.document(title=f'Ignite Status Dashboard')
        self.clients = clients

    def checkbox(type,checked,description):
        with div ():
            raw(f"""<label><input type="checkbox" class="checkbox" value="offertype{type}" {checked}> {description}</label>""")


    def doc(self):
        with self.Dashboard.head:
            meta (name="viewport", content="width=device-width, initial-scale=1")
            link (rel="stylesheet", href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css")
            script (src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js")
            script (src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js")
            script (src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js")
            script (src="https://kit.fontawesome.com/a076d05399.js")
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
            .fa-crosshairs {
            font-size: 15 px;
            
            }
            .dealer_name {
            width: 350px;
            }
            .fa-fire-alt {
            font-size:30px;
            }
            .fire_button_client {
            position: relative;
            top: 10px;
            }
            .fire_button_dealer {
            position: relative;
            top: 0px;
            }
            """, is_pretty = True)
            
        with self.Dashboard:
            with div(cls="container"):
                for c in self.clients:
                    with div(cls=f'{c.Name}'):
                        with div( cls='btn btn-primary', data_toggle="collapse", data_target=f"#ClientID{c.ClientID}"):
                            i(cls="far fa-arrow-alt-circle-down")
                            a(c.Name)
                        with a(cls="fire_button_client" , style="margin: 0px 0px 0px 0px;",href=f"https://dealermarketingportal.azurewebsites.net/Authenticate?userID={c.WebID}&dealerWebID=None"):
                            if c.IsActive == False:
                                i(cls="fas fa-fire-alt" , style="color:black;")
                            else:
                                i(cls="fas fa-fire-alt" , style="color:red;")
                        with div(cls='collapse', id=f"ClientID{c.ClientID}"):
                            with div(cls="d-flex flex-wrap"):
                                with div(cls="d-flex flex-column ",style="margin: 0px 10px 0px 0px;"):
                                    div(f'ClientID: {c.ClientID}')
                                    div(f'Location: {c.Location}')
                                    div(f'Phone: {c.Phone}')
                                    div(f'Website: {c.Website}')
                                    with div():
                                        if f'{c.IsActive}' == 'True':
                                            emoji = i(cls="far fa-grin-beam")
                                        else:
                                            emoji = i(cls="far fa-sad-tear")
                                        a(f'IsActive: {c.IsActive}')
                                    div(f'CreatedDT: {c.CreatedDT.strftime("%Y/%m/%d")}')
                                with div(cls="d-flex flex-column ",style="margin: 0px 10px 0px 0px;"):
                                    if c.Batch == None:
                                        div(f'BatchID: Shit Broke')
                                    else:
                                        with div():
                                            try:
                                                if c.Batch.BatchDetails.ExportJobEndDT.strftime("%Y/%m/%d") == datetime.datetime.today().strftime("%Y/%m/%d"):
                                                    emoji = i(cls="far fa-grin-beam")
                                                else:
                                                    emoji = i(cls="far fa-angry")
                                            except:
                                                emoji = i(cls="far fa-angry")
                                            a(f'BatchID: {c.Batch.BatchID}')
                                        try:
                                            div(f'VehicleJobStartDT: {c.Batch.BatchDetails.VehicleJobStartDT.strftime("%Y/%m/%d")}')
                                        except:
                                            div(f'VehicleJobStartDT: {c.Batch.BatchDetails.VehicleJobStartDT}')
                                        try:
                                            div(f'VehicleJobEndDT: {c.Batch.BatchDetails.VehicleJobEndDT.strftime("%Y/%m/%d")}')
                                        except:
                                            div(f'VehicleJobStartDT: {c.Batch.BatchDetails.VehicleJobEndDT}')
                                        try:
                                            div(f'OfferJobStartDT: {c.Batch.BatchDetails.OfferJobStartDT.strftime("%Y/%m/%d")}')
                                        except:
                                            div(f'OfferJobStartDT: {c.Batch.BatchDetails.OfferJobStartDT}')
                                        try:
                                            div(f'OfferJobEndDT: {c.Batch.BatchDetails.OfferJobEndDT.strftime("%Y/%m/%d")}')
                                        except:
                                            div(f'OfferJobEndDT: {c.Batch.BatchDetails.OfferJobEndDT}')
                                        try:
                                            div(f'ExportJobStartDT: {c.Batch.BatchDetails.ExportJobStartDT.strftime("%Y/%m/%d")}')
                                        except:
                                            div(f'ExportJobStartDT: {c.Batch.BatchDetails.ExportJobStartDT}')
                                        try:
                                            div(f'ExportJobEndDT: {c.Batch.BatchDetails.ExportJobEndDT.strftime("%Y/%m/%d")}')
                                        except:
                                            div(f'ExportJobEndDT: {c.Batch.BatchDetails.ExportJobEndDT}')

                        

                            
                            with div(cls='d-flex flex-wrap '):
                                for d in c.Dealers:
                                    with div(cls="d-flex flex-wrap dealer_name" ,style="margin: 10px 10px 0px 0px;"):
                                        with div(cls=""):
                                            i(cls="far fa-arrow-alt-circle-down",style="font-size:25px", data_toggle="collapse", data_target=f"#DealerID{d.DealerID}")
                                            a(f'Name: {d.Name}')
                                        with a(cls="fire_button_dealer",style="margin: 0px 0px 0px 0px;",href=f"https://dealermarketingportal.azurewebsites.net/Authenticate?userID={c.WebID}&dealerWebID={d.WebID}"):
                                            if d.IsActive == False:
                                                i(cls="fas fa-fire-alt", style="color:black; margin: 0px 0px 0px 10px;")
                                            else:
                                                i(cls="fas fa-fire-alt", style="color:red; margin: 0px 0px 0px 10px;")
                                        with div(cls='collapse', id=f"DealerID{d.DealerID}"):
                                            with div(cls="d-flex flex-row"):
                                                for st in d.StockTypes:
                                                    if st.StockType == 'New':
                                                        div(f'New Vehicles Ran: YES',style="margin: 0px 5px 0px 0px;")
                                                    elif st.StockType == 'Used':
                                                        div(f'Used Vehicles Ran: YES')
                                            div(f'DealerCode: {d.DealerCode}')
                                            div(f'DealerID: {d.DealerID}')
                                            div(f'City: {d.City}')
                                            div(f'ZipCode: {d.ZipCode}')
                                            div(f'County: {d.County}')
                                            div(f'MSAccountID: {d.MSAccountID}')
                                            div(f'VAutoFilename: {d.VAutoFilename}')
                                            div(f'HomeNetFilename: {d.HomeNetFilename}')
                                            div(f'ExportFilename: {d.ExportFilename}')
                                            with div():
                                                if f'{d.IsActive}' == 'True':
                                                    emoji = i(cls="far fa-grin-beam")
                                                else:
                                                    emoji = i(cls="far fa-sad-tear")
                                                a(f'IsActive: {d.IsActive}')
                                            div(f'CreatedDT: {d.CreatedDT.strftime("%Y/%m/%d")}')
                                            hr()
                        hr()

                    
            

        return self.Dashboard

    
#text = SpecialsPagev1()

#print(text.doc())
    
    

    
