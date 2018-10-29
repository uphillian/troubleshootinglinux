#!/usr/bin/env python

import os
import time

pid = os.fork()
if pid == 0:
  print("Child")
  pid = os.fork()
  if pid == 0:
    print("Grandchild")
    while True:
      time.sleep(1)
else:
  print("Parent, Child PID: %s" % pid)
