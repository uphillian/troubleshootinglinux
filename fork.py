#!/usr/bin/env python

import os
import time

pid = os.fork()
if pid == 0:
  print("Child")
  while True:
    time.sleep(1)
else:
  print("Parent, Child PID: %s" % pid)
