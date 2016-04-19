#!/usr/bin/python

import thread
import time

maxThreads = 10

def printThreadName(threadName):
   count = 0
   while count < 10:
      time.sleep(1)
      count += 1
      print("%d: %s\n" % ( thread.get_ident(), time.ctime(time.time()) ) )
   thread.exit()

#Create Threads
threads = []
try:
  count = 0
  while count < maxThreads:
    tid = thread.start_new_thread( printThreadName, (count,) )
    print("TID: %s\n" % tid)
    threads.append(tid)
    count += 1
    
except:
  print "Error: unable to start thread"

while 1:
   time.sleep(2)
   for t in threads:
     print(t) # not right, need to know how to do that....
   print(threads)
   pass
