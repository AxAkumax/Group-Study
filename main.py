import urllib
from Table import Table
from Course import Course
from Person import Person
import Calendar

def run():
    #main function
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    
    p = Person(first_name, last_name, email, password)
    print(f"Hello {first_name} {last_name}")
    print(f'Verify email: {email}')
    verify = input()
    if verify == 'Y':
        print("Email verified")
    else:
        verify = False
    print('ACCOUNT CREATED')
    print('---------------')
    
    print('Making schedule')
    print()
    print('Input 5-digit course code for Fall 2022 quarter, write QUIT when done: ')
    userInput = input()
    x = Table(1,7.20,20.50)
    m = []
    while(userInput != 'QUIT'):
        y = Calendar.getCourse(userInput)
        m.append(y)
        userInput = input()
    #print(x.get_times())
    '''b = Calendar.getCourse(68010) #psych 7a: tues thurs
    a = Calendar.getCourse(44328) #monday wednesday friday math 3a
    c = Calendar.getCourse(60004)#anthro 2a tues thursd 9am'''
    
    for key in Calendar.weekly_schedule:
        x.create_schedule(m)
        x.build_schedule()
        Calendar.weekly_schedule[key] = x
        print(key)
        x.print_table()
    #m = [b,a,c]
    #print(x.create_schedule(m))
    #x.build_schedule()
    #x.print_table()

if __name__=='__main__':
    run()