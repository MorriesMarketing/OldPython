import calendar
import datetime
import time
from time import sleep

class Today():

    def __init__(self):
        self.today = datetime.datetime.today()
        self.today_year = self.today.year
        self.today_month = self.today.month
        self.today_day = self.today.day
        self.prev_year = self.today.year
        self.prev_month = self.today.month - 1
        self.next_year = self.today.year
        self.next_month = self.today.month + 1
        self.month_check()
        self.next_month_format = datetime.datetime(self.next_year, self.next_month,1).strftime("%B")
        self.prev_month_format = datetime.datetime(self.prev_year, self.prev_month,1).strftime("%B")
        self.today_month_format = self.today.strftime("%B")
        self.last_day = self.end_of_month()
        self.today_date_format = self.today.strftime("%Y/%m/%d")

    def month_check(self):
        if self.today_month == 12:
            self.next_month = 1
            self.next_year = today_year + 1
        if self.today_month == 1:
            self.prev_month = 12
            self.prev_year = today_year -1
        
    def end_of_month(self):
        end_of_month = calendar.monthrange(self.today_year,self.today_month)[1]
        today = self.today_day
        if today == end_of_month:
            self.last_day = True
            return self.last_day

    def time_taken(function, *args):
        time_start = time.time()
        print(f'\nSTARTING {function.__name__}: \t{datetime.datetime.today()}\n')
        function(*args)
        time_end = time.time()
        time_elapsed = time_end - time_start
        print(f'\nSUCCESS! {function.__name__} Elapsed: \t{time_elapsed}\n')

    def date_x_days_ago(Minus_Days, Year, Month, Day):
        today_date = datetime.datetime.today().strftime("%Y/%m/%d")
        calculated_date = datetime.datetime.today() - datetime.timedelta(Minus_Days)
        formated_calculated_date = calculated_date.strftime("%Y/%m/%d")
        provided_date = datetime.datetime(Year,Month,Day).strftime("%Y/%m/%d")

        if today_date >= filename_date >= last_weeks_date:
            return True
        else:
            return False



today = Today()
x = today.today_date_format
print(x)
