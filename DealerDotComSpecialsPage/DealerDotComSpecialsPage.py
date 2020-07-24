from ObjectCreator import *

from Pages import *

class SpecialsPage():
     def __init__(self):
         self.clients = ObjectCreator.create_clients_dealers_vehicles_offers(TestActive=True)
    
    

def main():
    print('Running Main Function')
    specials = SpecialsPage()

    print('Starting Html Builder Function')
    for c in specials.clients:
        if c.Batch != None:
            print(f'{c}/n No Batch Found')
            #c.IsActive = 0
        elif c.IsActive == 1:
            #print(f'/n{c}/n {c.Batch.MaxBatchID}')
            for d in c.Dealers:
                if d.ActiveSpecialsPage == 1:
                    if d.GroupSite == 1:
                        html = SpecialsPagev1(c.Vehicles,d,c.Years,c.Models,c.Makes)
                        print(d.DealerName)
                        txt = open(f'F:/SpecialsPage/{d.DealerName}.html',"w+")
                        txt.write(str(html.doc()))
                        txt.close()
                    else:
                        html = SpecialsPagev1(d.Vehicles,d,d.Years,d.Models,d.Makes)
                        print(d.DealerName)
                        txt = open(f'F:/SpecialsPage/{d.DealerName}.html',"w+")
                        txt.write(str(html.doc()))
                        txt.close()
                            


if __name__ == "__main__":
    main()