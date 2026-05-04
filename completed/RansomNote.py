   
# 383. Ransom Note
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # build dicts 
        rd = {}
        md = {}

        for i in ransomNote:
            rd[i] = rd.get(i,0) + 1
    
        for i in magazine:
            md[i] = md.get(i,0) + 1

        for key in rd.keys():
            if key not in md or rd[key] > md[key]: # is a in mag?
                return False
        return True 
    