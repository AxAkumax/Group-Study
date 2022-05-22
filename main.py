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
    c = Calendar.getCourse(60004)
    m = [b,a,c]
    print(x.create_schedule(m))
    x.build_schedule()
    x.print_table()

if __name__=='__main__':
    run()