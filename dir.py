#!/usr/bin/env python

import time
import os

os.chdir('/srv/h')
f=open('/srv/h/j','a')
while 1:
  f.write('Hello\n')
  f.flush()
  time.sleep(2)

