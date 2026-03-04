class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)
        if 0 not in nums_set: return 0

        nums.sort() #we sort to prepare indexing, ensuring index 0 contains 0. 
        for i in range(len(nums)):
            if nums[i]+1 not in nums_set: # O(n) look up time 
                return i+1 # return missing value
                