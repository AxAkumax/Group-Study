from tabulate import tabulate
#The following module contains a class and its member functions associating with a Table
#The Table Class contains a 24-max schedule on an hourly basis for users to make their schedule

class Table:
    def __init__(self, time_spacing):
        #The maximum hours a person can make a schedule for is 24
        #The person time spacing must be at mostly every 2 hours
        try:
            assert time_spacing>0 and time_spacing<=2, "Invalid Time Spacing"
            self._max_hours = 24
            self._time_spacing = time_spacing
        except:
            self.reset()

    def reset(self):
        self._time_spacing = float(input("Spacing The Time In the Day: "))
        while self._time_spacing<=0 and self.time_spacing>2:
            print("INVALID INPUT"+"\n"+"Maximum Hours Must Be Greater than 0 and less than or equal to 2")
            self._time_spacing = float(input("Spacing The Time In the Day: "))
        