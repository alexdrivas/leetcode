class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        l = 0
        r = k-1
        minimum = 10**5 + 1
        amount = 0 
        nums.sort()

        while r < len(nums):
            amount = nums[r] - nums[l] # get sum of window 
            minimum = min(amount, minimum)
            r+=1
            l+=1
        return minimum