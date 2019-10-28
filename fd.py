#!/usr/bin/env python
import datetime
import os
import time
filename='fd-example'
with open(filename,'w') as f:
  if os.path.isfile(filename):
    print("Inode of %s is %s" % (filename,os.stat(filename).st_ino))
    os.unlink(filename)
  while True:
    time.sleep(1)
    f.write("%s\n" % str(datetime.datetime.now()))
    f.flush()
