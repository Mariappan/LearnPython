#!/usr/bin/env python3

def double_char(str):
  strr = ""
  for i in str:
    strr += i
    strr += i
  
  return strr

print (double_char("Hi There"))
