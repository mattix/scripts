#!/bin/python3
import subprocess

status = subprocess.getoutput('acpi')
formatted = status.replace('Charging', '').replace('Discharging', '').replace('until charged', '').replace('remaining', '').replace('Battery 0:', '').replace(',', '')
print(formatted)

# status = '' if v['POWER_SUPPLY_STATUS'] is 'Charging' else ''
#print("{0} {1:3d} %".format(status, int(percent)))
