from tabulate import tabulate
from Course import Course
import math
#The following module contains a class and its member functions associating with a Table
#The Table Class contains a 24-max schedule on an hourly basis for users to make their schedule

class Table:
    def __init__(self, time_spacing, start = 0.0, end = 24.0):
        #The maximum hours a person can make a schedule for is 24
        #The person time spacing must be at mostly every 2 hours
        try:
            assert time_spacing>0 and time_spacing<=2, "Invalid Time Spacing"
            self._max_hours = 24
            self._time_spacing = time_spacing
        except:
            self.reset()
        
        table_hour = self._max_hours/self._time_spacing
        self.set_start_end(start,end)
        self.create_time_table_decimal()
        self.create_string_table()

    def set_start_end(self,start,end):
        #decimal value 2.30 = 2:30 A.M   13.21 = 1:21 P.M
        if (start>=0 and start<=24 and end>=0 and end<=24):
            self._start_num = start
            self._end_num = end
        else:
            raise AssertionError("Invalid Time Input")
    
    def create_time_table_decimal(self):
        #creates an array of times in decimals for the time schedule
        self._table_num = []
        start = self._start_num
        while start<=self._end_num:
          if start%1 >= 0.60:
              value = start+1
              start = value - start%1
          self._table_num.append(start)
          start+=self._time_spacing
        return self._table_num
    
    def create_string_table(self):
        #makes an array of strings with the time, e.g: 2.0 = 2:00 pm
        self._str_times = []
        for i in self._table_num:
            time_before_colon = int((math.modf(i))[1])
            time_after_colon = round((math.modf(i))[0],2)
            time_value = ""
            value = ""
            if time_after_colon == 0:
                value = "00"
            elif (time_after_colon*100)<10:
                value+="0"+(str(time_after_colon*100)[:1])
            else:
                value = (str(time_after_colon*100)[:2])

            if time_before_colon>12:
                time_value+=str(time_before_colon-12)+":"+value+" P.M"
            elif time_before_colon == 12:
                time_value+=str(time_before_colon)+":"+value+" P.M"
            else:
                time_value+=str(time_before_colon)+":"+value+" A.M"
            self._str_times.append(time_value)
        
        return self._str_times

    def get_times(self):
        return self._str_times

    def reset(self):
        self._time_spacing = float(input("Spacing The Time In the Day: "))
        while self._time_spacing<=0 and self.time_spacing>2:
            print("INVALID INPUT"+"\n"+"Maximum Hours Must Be Greater than 0 and less than or equal to 2")
            self._time_spacing = float(input("Spacing The Time In the Day: "))
        