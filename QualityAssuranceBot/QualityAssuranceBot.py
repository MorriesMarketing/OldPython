from ObjectCreator import *
from ComparisonObject import *



class Group():
     def __init__(self):
         self.clients = ObjectCreator.create_clients_dealers_vehicles_offers()

def comparison(group1, group2, identifier, identifier2, UniqueID):
    total = 0
    score = 0
    changed_attributes = []
    tally = {
        'changed_attributes' : changed_attributes
        }
    modifier_active = False
    if isinstance(group1,list):
        pass
    else:
        for attr, value in group1.__dict__.items():
            if attr == UniqueID:
                modifier_active = True

    if modifier_active == True or isinstance(group1,list):
        for attr, value in group1.__dict__.items():
            for attr2, value2 in group2.__dict__.items():
                if attr == UniqueID and attr2 == UniqueID and value == value2:
                    for a, v in group1.__dict__.items():
                        for a2, v2 in group2.__dict__.items():
                            if attr == attr2:
                                if isinstance(value,list):
                                    print('Running List')
                                    cursed_tally = comparison(group1.__dict__[attr], group2.__dict__[attr2], identifier, identifier2, UniqueID)
                                    changed_attributes += cursed_tally['changed_attributes']
                                elif value != value2:
                                    changed_attributes.append(f'{group1.identifier}: {attr}_{value} != {group2.identifier}: {attr2}_{value2}')
    else:   
        for attr, value in group1.__dict__.items():
            for attr2, value2 in group2.__dict__.items():
                if attr == attr2:
                    if isinstance(value,list):
                        print('Running List')
                        cursed_tally = comparison(group1.__dict__[attr], group2.__dict__[attr2], identifier, identifier2, UniqueID)
                        changed_attributes += cursed_tally['changed_attributes']
                    elif value != value2:
                        changed_attributes.append(f'{identifier}: {attr}_{value} != {identifier2}: {attr2}_{value2}')
    tally['changed_attributes'] = changed_attributes
    return tally


#def comparison(group1, group2, modifier):
#    
#   
#
#    total = 0
#    score = 0
#    changed_attributes = []
#    complex_attributes = []
#    list_attributes = []
#
#    tally = {
#        'score' : score,
#        'total' : total,
#        'changed_attributes' : changed_attributes,
#        'complex_attributes' : complex_attributes,
#        'list_attributes' : list_attributes,
#        }
#
#    for attr, value in group1.__dict__.items():
#        for attr2, value2 in group2.__dict__.items():
#            if attr == attr2:
#                total += 1
#                if value == value2:
#                    score += 1
#                elif type(value) is str or type(value) is int or type(value) is float:
#                    print(f'Group1:{attr} & Group2:{attr2} are objects')
#                    complex_attributes.append(attr)
#                    score += 1
#                elif isinstance(value,list):
#                    list_attributes.append(attr)
#                    score += 1
#                else:
#                    changed_attributes.append(attr)
#
#                for a in complex_attributes:
#                     cursed_tally = comparison(group1.__dict__[a],group2.__dict__[a],modifier)
#                     score += cursed_tally['score']
#                     total += cursed_tally['total']
#                     changed_attributes += cursed_tally['changed_attributes']
#                     complex_attributes += cursed_tally['complex_attributes']
#                     list_attributes += cursed_tally['list_attributes']
#
#                for l in list_attributes:
#                    print(l)
#                    for object in group1.__dict__[l]:
#                        for object2 in group2.__dict__[l]:
#                            if object.__dict__[modifier] == object2.__dict__[modifier]:
#                                
#                                for attr, value in object.__dict__.items():
#                                    for attr2, value2 in object2.__dict__.items():
#                                        if attr == attr2:
#                                            
#                                            total += 1
#                                            if value != value2:
#                                                print(f'Group1:{attr} != Group2:{attr2}')
#                                            else:
#                                                score += 1
#                                                cursed_tally = comparison(object,object2,modifier)
#                                                score += cursed_tally['score']
#                                                total += cursed_tally['total']
#                                                changed_attributes += cursed_tally['changed_attributes']
#                                                complex_attributes += cursed_tally['complex_attributes']
#                                                list_attributes += cursed_tally['list_attributes']
#                        
#    tally['score'] = score
#    tally['total'] = total
#    tally['failed_attributes'] = failed_attributes
#    tally['complex_attributes'] = complex_attributes
#    tally['list_attributes'] = list_attributes
#    
#    
#    return tally

def create_comparison_class():
    group_1 = Group()
    for x in group_1.clients:
        x.Name = 'ZZ'

    sleep(5)
    group_2 = Group()


    for c in group_1.clients:
        for c2 in group_2.clients:
            if c.ClientID == c2.ClientID:

                x = comparison(c,c2,c.ClientID,c2.ClientID, 'VINOffer')
                print(f'{c.ClientID}: {x}')
                


def test_run():
    group_1 = Group()
    for c in group_1.clients:
        for attr, value in c.__dict__.items():
            print(attr, value)
def main():
    print('Running Main Function')
    create_comparison_class()


if __name__ == "__main__":
    main()
