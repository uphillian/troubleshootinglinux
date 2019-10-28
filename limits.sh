#!/bin/bash
for i in {1..41}
do
  echo -n "$i "
  sleep 10 &
done
echo
