def string_splosion(str):
  newstr = ""
  for i in range(len(str) + 1):
    newstr += str[:i]
  
  return newstr

