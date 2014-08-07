#!/usr/bin/env python3

def end_other(a, b):
  a = a.lower()
  b = b.lower()
  
  if len(a) < len(b):
    if a == b[-len(a):]:
      return True
    else:
      return False
  else:
    if b == a[-len(b):]:
      return True
    else:
      return False
      
