#!/usr/bin/env python3

def cat_dog(str):
  cat_count = 0
  for i in range(len(str)-2):
    if str[i:i+3] == "cat":
      cat_count += 1
  
  dog_count = 0
  for i in range(len(str)-2):
    if str[i:i+3] == "dog":
      dog_count += 1
  
  if cat_count == dog_count:
    return True
  else:
    return False

