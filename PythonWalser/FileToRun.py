#import R_VehicleSpecialsNew
import datetime

def main():
    today_date = datetime.datetime.today().strftime("%Y/%m/%d")
    calculated_date = datetime.datetime.today() - datetime.timedelta(7)
    last_weeks_date = calculated_date.strftime("%Y/%m/%d")
    filename_date = datetime.datetime(2020,9,15).strftime("%Y/%m/%d")
    test_date = datetime.datetime(int('2020-09-15')).strftime("%Y/%m/%d")

    print(today_date)
    print(last_weeks_date)
    print(filename_date)
    print(test_date)
    if today_date >= filename_date >= last_weeks_date:
        print('True')
main()