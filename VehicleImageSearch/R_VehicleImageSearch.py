from ObjectCreator import *

def main():
    print('Running Main Function')
    TestActive = False
    objects = ObjectCreator(TestActive)
    
    #object = objects.create_objects()
    objects.gather_vdp_website_list()
    #objects.combine_objects()
                         
if __name__ == "__main__":
    main()