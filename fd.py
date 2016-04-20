#!/usr/bin/env python
import time
import datetime
with open('/srv/fd','w') as f:
  while True:
    time.sleep(1)
    f.write("%s\n" % str(datetime.datetime.now()))
    f.flush()
