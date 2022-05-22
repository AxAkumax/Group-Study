import urllib.request
import json

class Course:
    def __init__(self, name, time, meet_days):
        self.name = name
        self.time = time
        self.meet_days = meet_days

    def get_name(self):
        return self.name

    def get_time(self):
        return self.time

    def get_meet_days(self):
        return self.meet_days
