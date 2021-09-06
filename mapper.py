#!/usr/bin/python3
# import numpy as np
import sys
import json
import datetime
import re

for line in sys.stdin:
  try:
    record = json.loads(line)
    record_is_clean = is_clean(record)
    if record_is_clean:
      first_task(record,sys.argv[1])
    else:
      continue
  except Exception as e:
    continue    
    
def first_task(record,word):
	
# Edit: 1
	
	
	
	
	
