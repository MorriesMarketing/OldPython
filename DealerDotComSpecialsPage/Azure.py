from azure.storage.blob import BlobClient
from azure.storage.blob import ContentSettings

blob = BlobClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;AccountName=ignitespecials;AccountKey=ybwXJCSlLeZ1V9njLf7zmlyiRiA4TQG8HQcXaVIbN8AeLEGJD+vbxG4nNyaFCROgYfRpRE/qa94QRoAagY+FVQ==;EndpointSuffix=core.windows.net", container_name="$web", blob_name="Walser_Subaru_Burnsvilletext.html")
#blob.delete_blob()
with open("F:/SpecialsPage/Walser Subaru St. Paul.html", "rb") as data:
    blob.upload_blob(data,content_settings=ContentSettings(content_type='text/html'))

