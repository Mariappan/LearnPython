# Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.

# has22([1, 2, 2]) → True
# has22([1, 2, 1, 2]) → False
# has22([2, 1, 2]) → False

def has22(nums):
  found = False
  
  for i in nums:
    if found == True:
      if i == 2:
        return True
      else:
        found = False
        continue
        
    if i != 2:
      continue
    
    found = True
    
  return False