def array123(nums):
  if len(nums) < 3:
    return False
  
  for i in range(len(nums) - 3 + 1):
    short = nums[i:i+3]
    
    if short == [1,2,3]:
      return True
      
  return False
