class Solution:
    def maxArea(self, height: List[int]) -> int:
        first = 0
        last = len(height) - 1
        area = 0
        while first < last:
           width = last - first
           if height[first] < height[last]:
               minHeight = height[first]
               first += 1
           else:
               minHeight = height[last]
               last -= 1     

           area = max(width * minHeight, area)

        return area
      