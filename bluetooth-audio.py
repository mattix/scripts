#!/bin/python3
import subprocess
import sys

#device = '00:16:94:1A:C9:AA'
device = '2C:41:A1:82:BB:D9'

command = 'bt-device -i {0} | grep -c "Connected: 1"'.format(device)
connected = int(subprocess.getoutput(command)) > 0

if len(sys.argv) > 1 and sys.argv[1] == '1':
    command = 'bt-device -{0} {1}'.format('d' if connected else 'c', device)
    subprocess.getoutput(command)

print('' if connected else '<span color="#4f4f4f"></span>')
