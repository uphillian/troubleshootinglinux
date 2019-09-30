#!/usr/bin/python

import thread
import threading
import time

maxThreads = 50

def printThreadName(threadName):
   count = 0
   while count < 10:
      time.sleep(100)
      count += 1
   thread.exit()

#Create Threads
threads = []
try:
  count = 0
  while count < maxThreads:
    tid = thread.start_new_thread( printThreadName, (count,) )
    threads.append(tid)
    count += 1
    
except:
  print "Error: unable to start thread"

while 1:
   time.sleep(20)
   pass
