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
    return ''

status = subprocess.getoutput('acpi')
splitted = status.split(' ')
percent = int(splitted[3].replace('%,', ''))
status_icon = get_status_icon(percent)

formatted = status.replace(
    'Charging', '').replace(
    'Discharging', status_icon).replace(
    'until charged', '').replace(
    'remaining', '').replace(
    'Battery 0:', '').replace(
    ',', '')
print(formatted)

# status = '' if v['POWER_SUPPLY_STATUS'] is 'Charging' else ''
#print("{0} {1:3d} %".format(status, int(percent)))
