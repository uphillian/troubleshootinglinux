#!/usr/bin/env python

import os
import time

pid = os.fork()
if pid == 0:
  pid = os.fork()
  if pid == 0:
    print("I am the Grandchild, PID: %s\n" % os.getpid())
    while True:
      time.sleep(10)
  else:
    print("I am the Child, PID: %s, the Grandchild PID: %s\n" % (os.getpid(),pid))
else:
  print("I am the Parent, PID: %s, my Child PID: %s\n" % (os.getpid(),pid))
