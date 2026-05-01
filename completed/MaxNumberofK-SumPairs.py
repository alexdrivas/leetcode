# 1679. Max Number of K-Sum Pairs
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        """
        Sort the array first, then use converging left/right pointers.
        If the array is sorted and nums[l] + nums[r] is too big, which pointer should you move? 
        If it's too small?
        """

        output = 0
        nums = sorted(nums)
        l , r = 0, len(nums)-1

        while l < r: 
            
            if nums[l] + nums[r] > k:
                r-=1
            elif nums[l] + nums[r] < k:
                l+=1
            elif nums[l] + nums[r] == k:
                l+=1
                r-=1
                output+=1
            
    
                

        return output