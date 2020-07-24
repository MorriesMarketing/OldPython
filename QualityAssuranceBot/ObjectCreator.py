from I_SqlServer import *
from O_Batch import *
from O_Clients import *
from O_Dealers import * 
from O_Vehicles import *
from O_Offers import *
from ComparisonObject import *

class ObjectCreator():

    def __init__():
        pass

    @staticmethod
    def create_clients_dealers_vehicles_offers():

        print('Creating Vehicle Objects')
        data_table = SqlServer.PRD_PythonOffers_ReadData()
        data = Database.convert_table_to_dict(data_table)
        vehicles = Database.create_grouped_objects(data, ComparisonVehiclesOffers, 'VIN')
        
        print('Creating Batch Objects')
        data_table = SqlServer.PRD_Batch_RefreshCheck()
        data = Database.convert_table_to_dict(data_table)
        batches = Database.create_grouped_objects(data, Batch, 'ClientID')

        print('Creating Client Objects')
        data_table = SqlServer.PRD_Client_ReadData()
        data = Database.convert_table_to_dict(data_table)
        clients = Database.create_grouped_objects(data, Client, 'ClientID')

        for c in clients:
            for v in vehicles:
                if c.ClientID == v.ClientID:
                    c.Vehicles.append(v)
                    
        print('Clients Created')
        return clients

