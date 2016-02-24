import redis
import json
import time
import sys
import numpy  #import kinds of libraries we need

conn = redis.Redis()    #create connection
def getoutliers(y):   #define a function that can get the outliers in streaming
    numerics = map(lambda string:float(string),y)   #put every element of list into numerics
    mean = numpy.mean(numerics)     #get mean 
    stddev = numpy.std(numerics)    #get standard deviation
    outliers = filter(lambda x:(mean-x)>2 * stddev,numerics)  # obtain outliers which are more than
    
    return outliers                                                            # 2 standard deviations through filter function
    sys.stdout.flush()    #flush ouput buffer

while 1:

    pipe = conn.pipeline()         # credited to professor Mike Dewar

    keys = conn.keys()             # obtain the keys in connection
  
    values = conn.mget(keys)       # obtain the corresponding values
    

    try:
        intervals = [float(v) for v in values]  #tranverse the element in values and store them into delta
        
    except TypeError:
        print keys
        continue

    if len(intervals):   #if the length of intervals is greater than 0
        rate = sum(intervals)/float(len(intervals))   #rate equals summation divided by the length
        s=getoutliers(intervals)    #obtain outliers, if any, and print
        
        if s!=[]:   #if s isn't empty, then print s is a time interval which is more than 2 standard deviations
             print "%f is a time interval which is more than 2 standard deviations"%s
        time.sleep(5) #when we have alerts, sleep 5 seconds so that we can observe them clearly
    else:
        rate = 0

    print json.dumps({"rate":rate})

    time.sleep(2)

