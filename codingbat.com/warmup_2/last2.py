def last2(str):
  sub = str[-2:]
  str = str[:-2]
  found = 0
  
  for i in range(len(str)):
    if -1 != str.find(sub, i, len(str) - (i+1)):
      found += 1
      
  return str.count(sub)
