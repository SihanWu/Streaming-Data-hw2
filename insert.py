import json
import sys
import redis   #import the libraries that we need

conn = redis.Redis() #construct connection

while 1:
    line = sys.stdin.readline()   #read line by line from printout
    d = json.loads(line)    # transform line into json format
    time_interval = d["time_interval"]      # obtain the value of time interval
    time = d["t"]			#  obtain time 
    conn.setex(time, time_interval, 600)  # transfer  time and time interval
    print json.dumps({"time":time, "d":time_interval})  # transfer time and delta to json format to output
