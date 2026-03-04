class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # outter loop iterates over each element in the list 
        for i in range(len(nums)): 
            # Inner loop iterates over the remaining elements after 'i'
            for j in range(i + 1, len(nums)):
                # Checkif the sum equals the target
                if nums[i] + nums[j] == target:
                    #return the indicies of the two numbers
                    return [i, j]  