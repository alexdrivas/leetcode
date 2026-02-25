class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        modify nums1 in-place
        nums1 = [1,2,3,0,0,0], m = 3
        num2 = [2,5,6], n = 3 
        output = [1,2,2,3,5,6]
        merge, sort, remove zeros num n
        """
        for i in range(len(nums2)):
            nums1.append(nums2[i])
        nums1.sort()

        try:
            position = nums1.index(0) # find position of first 0 in the array
            for i in range(n):
                nums1.pop(position)
            print(nums1)
            return nums1
        except:
            return e