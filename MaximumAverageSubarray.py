class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        cur_sum = max_sum = sum(nums[:k])

        # loop over the number of times we'll move the window 
        for i in range(len(nums) - k):
            cur_sum += nums[i+k] - nums[i] # drop left value, add right value 
            max_sum = max(cur_sum, max_sum)

        return max_sum/k
        