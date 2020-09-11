from ObjectCreator import *
from azure.storage.blob import BlobClient
from azure.storage.blob import ContentSettings
from Pages import *

TestActive = False

class DashboardObjects():
     def __init__(self,TestActive):
         self.object  = ObjectCreator()
         self.clients = self.object.create_clients_dealers_vehicles_offers(TestActive)

def main(TestActive):
    print('Running Main Function')
    dashboard = DashboardObjects(TestActive)
    html = Dashboard(dashboard.clients)
    txt = open(f'F:/IgniteStatusPage/IgniteStatusPage.html',"w+")
    txt.write(str(html.doc()))
    txt.close()

    if TestActive:
        pass
    else:
        blob = BlobClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;AccountName=ignitespecials;AccountKey=ybwXJCSlLeZ1V9njLf7zmlyiRiA4TQG8HQcXaVIbN8AeLEGJD+vbxG4nNyaFCROgYfRpRE/qa94QRoAagY+FVQ==;EndpointSuffix=core.windows.net", container_name="$web", blob_name=f"IgniteStatusPage.html")
        blob.delete_blob()
        with open(f'F:/IgniteStatusPage/IgniteStatusPage.html', "rb") as data:
            blob.upload_blob(data,content_settings=ContentSettings(content_type='text/html'))
        print('Starting Html Builder Function')


if __name__ == "__main__":
    while True:
        try:
            today = Today()
            main(TestActive)
            print(datetime.datetime.now())
            minute = 2
            value = minute * 60
            sleep(value)
        except:
            print(f'An Error Occured{datetime.datetime.now()}')
            sleep(value)