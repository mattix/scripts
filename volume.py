#!/bin/python3
import subprocess
import re
import sys

with open('/tmp/logi.log', 'w+') as f:
    f.write(str(sys.argv))

if len(sys.argv) is 1:
    p_vol = re.compile('\d+%')
    p_mute = re.compile('Mute: no')
    info = subprocess.getoutput('pactl list sinks')
    volume = p_vol.findall(info)[0]
    status = '' if len(p_mute.findall(info)) > 0 else ''
    print("{0} {1}".format(status, volume))
