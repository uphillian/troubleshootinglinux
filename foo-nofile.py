#!/usr/bin/env python
from time import sleep

numfile = 50

i=0
f=[]
while 1:
  sleep(1)
  f.append(open("/tmp/foo-%s.txt" %i,'w'))
  i+=1
