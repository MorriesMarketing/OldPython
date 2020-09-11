from ObjectCreator import *
from azure.storage.blob import BlobClient
from azure.storage.blob import ContentSettings
from Pages import *

TestActive = False

class SpecialsPage():
    def __init__(self, TestActive):
        self.object = ObjectCreator()
        self.clients = self.object.create_clients_dealers_vehicles_offers(TestActive)
    
def main(TestActive):
    print('Running Main Function')
    specials = SpecialsPage(TestActive)

    print('Starting Html Builder Function')
    for c in specials.clients:
        if c.Batch == None:
            print(f'{c}/n No Batch Found')
            #c.IsActive = 0
        elif c.IsActive == 1:
            #print(f'/n{c}/n {c.Batch.MaxBatchID}')
            for d in c.Dealers:
                if d.ActiveSpecialsPage == 1:
                    if d.GroupSite == 1:
                        html = SpecialsPagev1(c.Vehicles,d,c.Years,c.Models,c.Makes)
                    else:
                        html = SpecialsPagev1(d.Vehicles,d,d.Years,d.Models,d.Makes)
                    print(d.DealerName)
                    txt = open(f'F:/SpecialsPage/{d.DealerName}.html',"w+")
                    txt.write(str(html.doc()))
                    txt.close()
                    if TestActive:
                        pass
                    else:
                        blob = BlobClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;AccountName=ignitespecials;AccountKey=ybwXJCSlLeZ1V9njLf7zmlyiRiA4TQG8HQcXaVIbN8AeLEGJD+vbxG4nNyaFCROgYfRpRE/qa94QRoAagY+FVQ==;EndpointSuffix=core.windows.net", container_name="$web", blob_name=f"{d.DealerName}.html")
                        blob.delete_blob()
                        with open(f'F:/SpecialsPage/{d.DealerName}.html', "rb") as data:
                            blob.upload_blob(data,content_settings=ContentSettings(content_type='text/html'))
                            


if __name__ == "__main__":
    main(TestActive)