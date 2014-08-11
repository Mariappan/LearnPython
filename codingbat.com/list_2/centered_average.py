# Return the "centered" average of an array of ints, which we'll say is the mean average of the values,
#  except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value,
#  ignore just one copy, and likewise for the largest value.
#  Use int division to produce the final average. You may assume that the array is length 3 or more.

# centered_average([1, 2, 3, 4, 100]) → 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3

def centered_average(nums):
  large = nums[0]
  for i in nums:
    if i > large:
      large = i
  
  small = nums[0]
  for i in nums:
    if i < small:
      small = i
      
  count = 0
  sum = 0
  leave = False
  
  for i in nums:
    if i == small:
      small = 0
      leave = True
    if i == large:
      large = 0
      leave = True
      
    if leave == False:
      sum += i
      count += 1
    leave = False
   
  return sum//count 
