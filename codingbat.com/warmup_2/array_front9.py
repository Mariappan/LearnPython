def array_front9(nums):
  l = 4
  if len(nums) < l:
    l = len(nums)
  
  found = 0
  for i in range(l):
    if nums[i] == 9:
      return True

  return False
