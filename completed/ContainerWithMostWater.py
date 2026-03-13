class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        maxA, area = 0, 0
        l, r = 0, len(height)-1

        # we have two pointers at the ends and decide which to move forwards
        while l < r:
            h = min(height[l],height[r])
            area = h * (r - l)
            maxA = max(maxA, area)
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return maxA

