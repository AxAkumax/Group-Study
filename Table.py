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
    
    def create_str_num_table_dict(self):
        str_num_dict = dict()
        for i in range(len(self._table_num)):
            dict[self._table_num[i]]=self._str_times[i]

    def create_schedule(self, course_list:Course):
        #makes a dictionary of the time schedule with the Course objects
        self._schedule = dict()
        for i in self._str_times:
            self._schedule[i]=[]

        for i in course_list:
            #type of i is a Course object
            #print(i.get_time())
            times = i.get_time().strip().split("-")
            value1,value2 = times[0],times[1]
            start, end = self.convert_string_to_decimal(value1,value2)
            self.array_schedule_times(start,i.get_name())

        return self._schedule
            # from 12:00AM-6:00PM = you get start = 12:00 & end =6:00
            
    #_____________________________helper functions for the schedule________________________________________

    def convert_string_to_decimal(self, start, end):
        #converts a time 5:00-7:00p to 12.00
        #pm must have p and am has none
        new_end = 0.0
        new_start = 0.0
        hour = "AM"
        if "p" in end:
            value = end[:len(end)-1]
            value1,value2 = value.strip().split(":")
            new_end = float(value1)+(float(value2)/100)+12
            hour = "PM"
        else:
            value1,value2 = end.strip().split(":")
        
        value1,value2 =  value.strip().split(":")
        new_start = float(value1)+(float(value2)/100)
        
        if hour=="PM" and new_start<12:
            new_start+=12
        #print(new_start, "=",new_end)
        return (new_start,new_end)

        

    def array_schedule_times(self,value:float, course_name:str):
        #takes a time and compares it with the time schedule and adds its it to the dictionary of times it falls under
        # ; e.g 12:10 falls under 12:00pm (course to that Time)

        for i in range(len(self._table_num)):
            if int(value)==int(self._table_num[i]):
                self._schedule[self._str_times[i]].append(course_name)

    def reset(self):
        #reset the entire table 
        self._time_spacing = float(input("Spacing The Time In the Day: "))
        while self._time_spacing<=0 and self.time_spacing>2:
            print("INVALID INPUT"+"\n"+"Maximum Hours Must Be Greater than 0 and less than or equal to 2")
            self._time_spacing = float(input("Spacing The Time In the Day: "))
        
        #delete all previously stored values
        self._str_times,self._table_num,self._schedule = [],[],dict()