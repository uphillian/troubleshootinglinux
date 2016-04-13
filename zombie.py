#!/usr/bin/env python

import os
import sys
import time
import signal

def sigcont(signum, frame):
  print("Received %d" % signum)

signal.signal(signal.SIGCONT, sigcont)
pid = os.fork()
if pid == 0:
  print("Child exiting")
  sys.exit(0)
else:
  print("Parent PID %s, Child PID: %s\nWaiting for Signal" % (os.getpid(),pid) )
  signal.pause()
  os.wait()
  print("Zombie is gone\n") 
  sys.exit(0)
  
