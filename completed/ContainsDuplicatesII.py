class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # we want the index and the value 
        # loop through array 
        # dictionary of {value, index}
        # if value not in dict, then add to dict 
        # if value in dict, compare differnece of the index to k (max step size) 
        # if >= return true 
        # if not update index. 
        
        d = {} #{value, index}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = i
            else: # value is in the dict
                if abs(d[nums[i]] - i) <= k:
                    return True
                else:
                    d[nums[i]] = i
        return False