class Solution:
    def mySqrt(self, x: int) -> int:
        # find some point (m) somewhere near x, binary search between 0 and x. 
        # if m^2 is > x then reduce the search space by moving the right 
        # if m^2 < x increase the search space my moving the left
        l, r = 0, x
        res = 0

        while l <= r:
            m = l + ((r-l)//2) # floor division to avoid overflow 
            if m*m > x:
                r = m - 1
            elif m*m < x:
                l = m + 1
                res = m
            else:
                return m
        return res

