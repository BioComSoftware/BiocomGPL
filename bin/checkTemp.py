#!/usr/bin/python2.7

import StringIO
import subprocess
import time
import datetime

logfile = open('/var/log/temp.log', 'a', 0)

loop = True
while loop:
    proc = subprocess.Popen('sensors',stdout=subprocess.PIPE)
    sense = proc.communicate()[0]
    sense = StringIO.StringIO(sense)
    print >>logfile, "----------"
    print >>logfile,  str(datetime.datetime.now().strftime('%Y-%m-%d:%Mmin.%Ssec'))
    for line in sense.readlines():
        line = ''.join(c for c in line if c not in "\n\r")
        if (("C" in line) and ('PCI' not in line)):
            print >>logfile, line
    time.sleep(15)        
#    loop = False
