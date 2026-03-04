class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in reversed(range(len(digits))): # reverse range indexing (3,2,1,0)
            # if val is 9
            if digits[i] == 9:
                digits[i] = 0
                # if index is 0, add element at index 0
                if i == 0:  
                    digits.insert(0,1)
            else: 
                digits[i] += 1 
                break
        return digits