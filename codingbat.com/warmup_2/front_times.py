def front_times(str, n):
  strlist = list(str)
  end = 3
  newstr = ""
  
  if len(str) < 3:
    end = len(str)
  
  str = "".join(strlist[0:end])
  
  for i in range(n):
    newstr += str
    
  return newstr
