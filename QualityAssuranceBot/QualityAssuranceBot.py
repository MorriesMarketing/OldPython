from ObjectCreator import *
from ComparisonObject import *
from O_Days import *



class Group():
     def __init__(self):
         self.dealers = ObjectCreator.create_clients_dealers_vehicles_offers()

def compare_objects(object1, object2, ColumnName):
    objects_report = {
    'list_of_current_objects' : [],
    'list_of_new_objects' : [],
    'list_of_old_objects' : [],
    'comparison_objects_report' : []
    }
    if ColumnName in object1.__dict__: 
        for attr, value in object1.__dict__.items():
            if attr == ColumnName:
                UniqueID = value

    for attr, value in object1.__dict__.items():
        
        for attr2, value2 in object2.__dict__.items():
            
            if attr == attr2:
                
                if isinstance(value,list):
                    #This is to check if the value is a list of objects
                    object_list = compare_list_of_objects(value, value2, ColumnName)
                    for item in object_list['list_of_current_objects']:
                        objects_report['list_of_current_objects'].append(item)
                    for item in object_list['list_of_new_objects']:
                        objects_report['list_of_new_objects'].append(item)
                    for item in object_list['list_of_old_objects']:
                        objects_report['list_of_old_objects'].append(item)
                    for item in object_list['comparison_objects_report']:
                        objects_report['comparison_objects_report'].append(item)



                elif type(value) is str or type(value) is int or type(value) is float:

                    #This is checking to see if the value is an object
                    if value == value2:
                        #Checks to see if both attribute and values match
                        pass
                    if value != value2:
                        
                        dict = [f'{UniqueID}',[[f'{attr}1', f'{value}'],[f'{attr2}2', f'{value2}']]]
                        if len(objects_report['comparison_objects_report']) == 0:
                            objects_report['comparison_objects_report'].append(dict)
                        else:
                            for y in objects_report['comparison_objects_report']:
                                if y[0] == dict[0]:
                                    y[1].append([f'{attr}1', f'{value}'])
                                    y[1].append([f'{attr2}2', f'{value2}'])
                                    
                                    
                            

    return objects_report


def compare_list_of_objects(list1, list2, ColumnName):

    object_list = []

    objects_report = {
    'list_of_current_objects' : [],
    'list_of_new_objects' : [],
    'list_of_old_objects' : [],
    'comparison_objects_report' : []
    }
    # Compares the list of objects to another list of objects by a designated column.
    # If the Column data matches for both objects it adds it to the object_list
    for object in list1:
        for object2 in list2:
            if object.__dict__[ColumnName] == object2.__dict__[ColumnName]:
                objects_report['list_of_current_objects'].append(object)
                object_list.append(object.__dict__[ColumnName])
                x = compare_objects(object, object2, ColumnName)
                for item in x['comparison_objects_report']:
                    objects_report['comparison_objects_report'].append(item)


    # checks the first list against the object_list.
    # If any values are not found they are placed into the list_of_old_objects
    for object in list1:
        if object.__dict__[ColumnName] not in object_list:
            objects_report['list_of_old_objects'].append(object)
    # checks the second list against the object_list.
    # If any values are not found they are placed into the list_of_new_objects
    for object in list2:
        if object.__dict__[ColumnName] not in object_list:
            objects_report['list_of_new_objects'].append(object)
    
    return objects_report

def create_comparison_class(TESTING):
    group_1 = Group()


    if TESTING:
        sleep_in_seconds = 5
        for s in range(sleep_in_seconds):
            print(f'{s}/{sleep_in_seconds}\r', end="")
            sleep(1)
    else:
        sleep_in_seconds = 3600
        for s in range(sleep_in_seconds):
            print(f'{s}/{sleep_in_seconds}\r', end="")
            sleep(1)
    

    group_2 = Group()

    for d in group_1.dealers:
        for d2 in group_2.dealers:
            if d.DealerID == d2.DealerID:
                print(f'Comparing {d.Name} & {d2.Name}')
                compared_report = compare_objects(d,d2, 'VINOffer')
                text = ''
                text += f'{d.DealerID}:\n'
                text += f'list_of_current_objects {compared_report["list_of_current_objects"]}\n'
                text += f'list_of_new_objects {compared_report["list_of_new_objects"]}\n'
                text += f'list_of_old_objects {compared_report["list_of_old_objects"]}\n'
                text += f'comparison_objects_report:\n'
                for x in compared_report["comparison_objects_report"]:
                    text += f'\n{x[0]}\n'
                    for y in x[1]:
                        text += f'\t{y}\n'
                today = Today()
                filename = f'{d.Name}_{today.today}'
                filename = filename.replace(' ','_')
                filename = filename.replace(':','_')
                
                if len(compared_report["comparison_objects_report"]) == 0:
                    print(f'no changes for {filename}')

                else:
                    print(f'{filename}')
                    filepath = f'F:/SpecialsPage/{filename}.txt'
                    print(filepath)
                    txt = open(filepath,"w+")
                    txt.write(str(text))
                    txt.close()

def test_run():
    group_1 = Group()
    for d in group_1.dealers:
        for attr, value in d.__dict__.items():
            print(attr, value)
def main():
    while True:
        print('Running Main Function')
        create_comparison_class(TESTING=False)


if __name__ == "__main__":
    main()
