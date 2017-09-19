#!/bin/python3
import subprocess

def get_status_icon(percent):
    if percent > 80:
        return ''
    if percent > 60:
        return ''
    if percent > 30:
        return ''
    if percent > 10:
        return ''
    return '<span color="#ff3300"></span>'

status = subprocess.getoutput('acpi')
statuses = status.split('\n')
index = 1 if len(statuses) > 1 and ('Unknown' in statuses[0] or 'unavailable' in statuses[0]) else 0
splitted = statuses[index].split(' ')
percent = int(splitted[3][0: splitted[3].find('%')])
time_left = splitted[4] if len(splitted) > 4 else ''

icon = '' if 'Charging' in status else get_status_icon(percent)
formatted = '{0} {1}% {2}'.format(icon, percent, time_left)

print(formatted)
