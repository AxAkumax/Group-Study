#The following module contains a class and its member functions associating with a Table
#The Table Class contains a 24-max schedule on an hourly basis for users to make their schedule

class Table:
    def __init__(self,max_hours, time_spacing):
        #The maximum hours a person can make a schedule for is 24
        #The person time spacing must be at mostly every 2 hours
        try:
            assert type(max_hours)==float,"Type of Hours is Invalid"
            assert max_hours>0 and max_hours<=24, "Invalid Maximum Hour Limit"
            assert time_spacing>0 and time_spacing<=2, "Invalid Time Spacing"
            self._max_hours = max_hours
            self._time_spacing = time_spacing
        except:
            self.reset()

    def reset(self):
        self._max_hours = float(input("Maximum Hour Limit: "))
        while self._max_hours<=0 and self._time_spacing>24:
            print("INVALID INPUT"+"\n"+"Maximum Hours Must Be Greater than 0 and less than or equal to 24")
            self._max_hours = float(input("Maximum Hour Limit: "))
        self._time_spacing = float(input("Spacing The Time In the Day: "))
        while self._time_spacing<=0 and self.time_spacing>2:
            print("INVALID INPUT"+"\n"+"Maximum Hours Must Be Greater than 0 and less than or equal to 2")
            self._time_spacing = float(input("Spacing The Time In the Day: "))
        