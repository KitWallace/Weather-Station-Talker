#!/usr/bin/python
import sys
import tty

def read_key() :
  last = 0
  tty.setcbreak(sys.stdin)

  while True :
    code = ord(sys.stdin.read(1)) 
    if (code== 53 and last==91) : 
      key = "left"
    elif (code==98) :
      key = "down"
    elif (code==54) :
      key = "right"
    elif (code==49) :
      key = "up"
    else :
      key = None
    last=code
    if not(key is None) :
       yield key


