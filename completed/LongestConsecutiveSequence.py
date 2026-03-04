class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        counter = 1
        max_counter = 1
        num_set = set(nums)
        
        for n in num_set:
            if n-1 not in num_set:              # start of a sequence
                counter = 1
                while n+counter in num_set:
                    counter+=1
            max_counter = max(max_counter, counter)
        return max_counter