class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        num_set = set(nums)
        res = ""
        output = []
        for num in nums:
            if num - 1 not in num_set and num + 1 not in num_set:
                # then it is alone "num" # add it to the array
                output.append(str(num))
                continue
            if num - 1 not in num_set: 
                # we are at the start of a sequence # add it to the array in the starting sequence 
                res = f"{num}->" 
                
            if num + 1 not in num_set:
                # we are at the end of the sequency # add it to the array 
                res = res + f"{num}"
                output.append(res)
        return output