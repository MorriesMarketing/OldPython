from Excel import *
from Outlook import *

'MNGeneralManagers@walser.com'

TestActive = True

def email(TestActive):
    excel = Excel()
    excel = excel.Walser_Ignite_Specials
    if TestActive:
        To = 'mmuhlenkort@walser.com'
        CC = ''
        Subject = 'New Inventory Specials'
        Body = 'This is a Test'
    else:
        To = 'MNGeneralManagers@walser.com'
        CC = 'awalser@walser.com;pswenson@walser.com;cswenson@walser.com;cray@walser.com;mprice@walser.com;psilovich@walser.com'
        Subject = 'New Inventory Specials'
        Body = ''
    #Email(to=To,cc=CC,subject=Subject,html_body=Body,attachment=excel)

email(TestActive)