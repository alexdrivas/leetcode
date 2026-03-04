class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        ndict={}
        for i in nums:
            ndict[i] = ndict.get(i,0) + 1

        for num, occurance in ndict.items():
            if occurance > n/2:
                return num