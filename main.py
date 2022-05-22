import urllib
from Table import Table
from Course import Course
import Calendar

def run():
    #main function
    x = Table(.20,12.0,14.50)
    print(x.get_times())
    
if __name__=='__main__':
    run()