#!/usr/bin/env python

import os
import time

pid = os.fork()
if pid == 0:
  print("Child")
  while True:
    time.sleep(10)
else:
  print("Parent, Child PID: %s" % pid)
  while True:
    time.sleep(10)
