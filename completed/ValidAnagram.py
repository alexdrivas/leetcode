class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        """
        Check the number of occurance of each character in the string. 
        We can easily insert, get values and compare dictionaries. 
        """
        ds = {}
        dt = {}

        for i in s:
            ds[i] = ds.get(i, 0) + 1
        for i in t:
            dt[i] = dt.get(i, 0) + 1

        if ds == dt: return True 
        return False