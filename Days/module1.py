import calendar
import datetime
import time

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
today = Today()
x = today.today_date_format
print(x)
