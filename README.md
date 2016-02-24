#streaming data
#Constructing system which can detect stream rate:

First, i wrote a program which can receive the the tweets sent by five official 
account(IBM, Google, Microsoft, Yahoo and Amazon).

Second, i used diff.py to obtain the time interval between two tweets. And then i used insert.py to insert time and 
time interval infomation to redis connection.

And then, i used avg.py to get the rate of my strea through calculating the ratio of the summation of every time interval
and the number of time interval.

#Building alert system:
I want to find outliers that are large than two standard deviations, which means if a time interval has 
more than two standard deviations difference from the mean of time interval. Then it is an unusual time interval, which 
means these five official accounts interact with followers more frequently or their companies release some new products 
or announcements.

Making them readable:

Inspried by the knowledge we learned in the first class, i decided to use websocket to show my result, and when we have 
alerts, the webpage will have alert information instead of normal rate information.


