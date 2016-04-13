#!/usr/bin/env python

import os
import sys
import time

pid = os.fork()
if pid == 0:
  print("Child")
  sys.exit(0)
else:
  print("Parent, Child PID: %s\nWaiting for Input" % pid)
  input = sys.stdin.readlines()
  os.wait()
  print("Zombie is gone\n") 
  sys.exit(0)
  
