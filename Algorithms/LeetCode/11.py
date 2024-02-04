# bad runtime

class Solution2(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        maxHeight = 0
        
        
        
        for x in range(0, len(height) - 1):
            for y in range((x+1), len(height)):
                
                # For each pair x, y calculate the area
                h = (y-x) * min(height[x], height[y])
                if h > maxHeight:
                    maxHeight = h
        
        return maxHeight


s = Solution2()
print(s.maxArea([1,8,6,2,5,4,8,3,7]) == 49)
