import urllib
from Table import Table
from Course import Course
import Calendar

def run():
    #main function
    x = Table(1,7.20,20.50)
    print(x.get_times())
    b = Calendar.getCourse(68010)
    a = Calendar.getCourse(44328)
    m = [b,a]
    print(x.create_schedule(m))

if __name__=='__main__':
    run()