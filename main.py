import urllib
from Table import Table
from Course import Course
import Calendar

def run():
    #main function
    x = Table(1,12.0,20.50)
    print(x.get_times())
    b = Calendar.getCourse(12120)
    a = Calendar.getCourse(13262)
    m = [b,a]
    print(x.create_schedule(m))

if __name__=='__main__':
    run()