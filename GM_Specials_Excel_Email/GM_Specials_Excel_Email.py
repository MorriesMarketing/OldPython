from Excel import Excel
from Outlook import *
from Page import *
from O_Days import *
TestActive = False

def main(TestActive):
    excel = Excel()
    excel = str(excel.Walser_Ignite_Specials)
    if TestActive:
        To = 'mmuhlenkort@walser.com'
        CC = ''
        Subject = 'New Inventory Specials'
        Body = Page()
    else:
        To = 'MNGeneralManagers@walser.com;KSGeneralManagers@walser.com'
        CC = 'awalser@walser.com;pswenson@walser.com;cswenson@walser.com;rlammle@walser.com;cray@walser.com;mprice@walser.com;psilovich@walser.com;klumsden@walser.com'
        Subject = 'Ignite New Inventory Specials'
        #Body = Page()
        #str(Body.doc())
    Email(to=To, cc=CC, subject=Subject, html_body='', attachment=excel)



if __name__ == "__main__":
    today = Today()
    while True:
        print(f'{today.today_year}-{today.today_month}-{today.today_day}')
        #pause.until(datetime(today.today_year, today.today_month, today.today_day, 7))
        #time = 5 *60
        #sleep(time)
        main(TestActive)
        break
