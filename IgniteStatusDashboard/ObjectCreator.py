from I_SqlServer import *
from O_Batch import *
from O_MaxBatch import *
from O_Clients import *
from O_Dealers import * 
from O_StockTypes import *

class ObjectCreator():
    #Project IgniteStatusDashboard

    def __init__(self):
        self.batches = ObjectCreator.create_list_of_objects(DatabaseTable=SqlServer.PRD_Batch_ReadData(), Object=Batch, Seperator=None)
        self.maxbatches = ObjectCreator.create_list_of_objects(DatabaseTable=SqlServer.PRD_Batch_ReadData(), Object=MaxBatch, Seperator=None)
        self.stocktypes = ObjectCreator.create_list_of_objects(DatabaseTable=SqlServer.PRD_CLientOffers_StockTypeSearch_ReadData(), Object=StockType, Seperator=None)
        self.clients = ObjectCreator.create_list_of_objects(DatabaseTable=SqlServer.PRD_Client_ReadData(), Object=Client, Seperator='ClientID')
        self.dealers = ObjectCreator.create_list_of_objects(DatabaseTable=SqlServer.PRD_Dealer_ReadData(), Object=Dealer, Seperator='DealerID')
        
    @staticmethod
    def create_list_of_objects(DatabaseTable,Object,Seperator):
        #print(f'Creating {DatabaseTable} Objects')
        data_table = DatabaseTable
        data = Database.convert_table_to_dict(data_table)
        if Seperator == None:
            object_list = Database.create_objects(data, Object)
        else:
            object_list = Database.create_grouped_objects(data, Object, Seperator)

        return object_list
    
    def create_clients_dealers_vehicles_offers(self, TestActive):

        if TestActive:
            for st in self.stocktypes:
                for d in self.dealers:
                    if st.DealerID == d.DealerID:
                        d.StockTypes.append(st)

            for mb in self.maxbatches:
                for b in self.batches:
                    if mb.BatchID == b.BatchID:
                        mb.BatchDetails = b

            for c in self.clients:
                for b in self.maxbatches:
                    if c.ClientID == b.ClientID:
                        c.Batch = b
                for d in self.dealers:
                    if c.ClientID == d.ClientID:
                        c.Dealers.append(d)
        else:
            for st in self.stocktypes:
                for d in self.dealers:
                    if st.DealerID == d.DealerID:
                        d.StockTypes.append(st)
            for mb in self.maxbatches:
                for b in self.batches:
                    if mb.BatchID == b.BatchID:
                        mb.BatchDetails = b

            for c in self.clients:
                for b in self.maxbatches:
                    if c.ClientID == b.ClientID:
                        c.Batch = b
                for d in self.dealers:
                    if c.ClientID == d.ClientID:
                        c.Dealers.append(d)
                    
        print('Clients Created')
        return self.clients

