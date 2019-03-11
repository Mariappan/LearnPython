class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        rowSize = len(grid)
        left_to = []
        top_to = []
        
        for i in range(rowSize):
            maxv = 0
            maxh = 0
            for j in range(rowSize):
                maxv = max(maxv, grid[i][j])
                maxh = max(maxh, grid[j][i])
            left_to.append(maxv)
            top_to.append(maxh)
        
        count = 0
        for i in range(rowSize):
            for j in range(rowSize):
                count += min(left_to[i], top_to[j]) - grid[i][j]
                
        return count
        
