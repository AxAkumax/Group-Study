import calendar
from Table import Table
from Course import Course
import urllib.request
import json

weekly_schedule = {'M': Table(1), 'Tu': Table(1), 'W': Table(1), 'Th': Table(1), 'F': Table(1)}
# for i in range(5):
#     weekly_schedule[calendar.day_name[i]] = Table.Table(1)


def process_meet_days(days):
    if days in weekly_schedule:
        return [days]

    elif days == 'MWF':
        return ['M', 'W', 'F']

    elif days == 'TuTh':
        return ['Tu', 'Th']


# given a course code, returns a course object with information about it
def getCourse(course_code):
    term = '2022Fall'
    url = f'https://api.peterportal.org/rest/v0/schedule/soc?term={term}&sectionCodes={course_code}'

    response = None
    course_data = None
    try:
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        json_text = response.read().decode(encoding = 'utf-8')
        course_data = json.loads(json_text)

    except urllib.error.URLError:
        print('FAILED')
    except urllib.error.HTTPError as e:
        print('FAILED')
        print('Status code: {}'.format(e.code))
    finally:
        if response != None:
            response.close()

    course = course_data['schools'][0]['departments'][0]['courses'][0]
    section = course['sections'][0]
    
    course_name = f"{section['sectionType']} {course['deptCode']} {course['courseNumber']}"
    meetings = section['meetings'][0]

    return Course(course_name, meetings['time'], process_meet_days(meetings['days']))
