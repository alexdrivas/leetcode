class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #return haystack.find(needle) #returns index of the first occurrance. 

        if needle == "":
            return 0
        for i in range(len(haystack) + 1 - len(needle)):
            if haystack[i: i + len(needle)] == needle: 
                return i 
        return -1