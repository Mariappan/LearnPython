#!/usr/bin/python

import re

class Time():
    def __init__(self, time):
        pattern = re.compile(r'(\d+):(\d+)([ap]m)')
        match = re.search(pattern, time)
        hr = int(match.group(1))
        hr = hr if hr != 12 else 0

        self.hours = hr
        self.minutes = int(match.group(2))
        self.time_period = match.group(3)

    def get_time_in_min(self):
        return (self.hours*60)+self.minutes

    def add_hours(self, hour):
        self.hours += hour

    def print(self):
        print("Time is " + str(self.hours)+":"+str(self.minutes) + self.time_period)

def CountingMinutes(str):
    str = str.split('-')
    start, end = Time(str[0]), Time(str[1])

    if start.time_period != end.time_period:
        end.add_hours(12)

    if end.get_time_in_min() < start.get_time_in_min():
        end.add_hours(24)

    time = end.get_time_in_min() - start.get_time_in_min()

    print("Time:", time)
    return time

assert(CountingMinutes("12:30pm-12:00am")==690)
assert(CountingMinutes("1:23am-1:08am")==1425)
assert(CountingMinutes("7:40am-8:20pm")==760)
assert(CountingMinutes("1:00am-12:00am")==1380)
