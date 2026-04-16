class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        my_list = list(set(nums))

        my_list = sorted(my_list, reverse = True)

        if len(my_list) < 3:
            return my_list[0]
        
        return my_list[2]