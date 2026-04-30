
# 387. FirstUniqueCharacterInAString

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        # char, count dict 
        # build diect 
        d = {}
        for i in s: # range(len())
            d[i]= d.get(i,0) + 1


        # find 1 occurance 
        for c,p in d.items():
            if p == 1:
                # look in string for index. 
                return s.index(c)
        return -1