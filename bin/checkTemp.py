#!/usr/bin/python2.7

import StringIO
import subprocess
import time
import datetime

# logfile = open('/var/log/temp.log', 'a', 0)

def getSensors():
    proc = subprocess.Popen('sensors',stdout=subprocess.PIPE)
    sense = proc.communicate()[0]
    sense = StringIO.StringIO(sense)
    result = []
    
    for line in sense.readlines():
        line = ''.join(c for c in line if c not in "\n\r")
#         line = line.encode('ascii')
        result.append(line)
    
    return result

    
if __name__ == "__main__":
    print getSensors()
