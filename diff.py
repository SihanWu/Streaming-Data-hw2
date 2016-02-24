import json
import sys  #import kinds of libraries

lastime = 0   #set lastime=0
while 1:
    line = sys.stdin.readline()  #read every line in standard in and reference to line
    d = json.loads(line)    #transform line into json format so that to print out
    if lastime == 0 :       # if this is the first time dectection
        lastime = d["t"]    #  then make lastime equals the value of time and start next loop
        continue
    time_interval = d["t"] - lastime   # calculate time interval
    print json.dumps({"time_interval":time_interval, "t":d["t"]})  #transform data into json for output
    sys.stdout.flush()
    lastime = d["t"]  #make lastime value equals the time now
