# 187. Repeated DNA Sequences

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        w = 10
        output = list()
        res= list()

        for i in range(0, len(s)- w+1):
            item = s[i:i+w]
            output.append(item)

        my_set = set()
        
        for i in output:
            if i in my_set:
                res.append(i)
            else: 
                my_set.add(i)
        return list(set(res))