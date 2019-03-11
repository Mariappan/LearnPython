class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if (len(height) == 0):
            return 0
        i=0
        j=len(height)-1
        max_value = min(height[i], height[j]) * (j - i)
        #print max_value, height, i, j
                     
        if (height[i] < height[j]):
            return max(max_value, self.maxArea(height[1:]))
        else:
            return max(max_value, self.maxArea(height[:-1]))
        return max_value
