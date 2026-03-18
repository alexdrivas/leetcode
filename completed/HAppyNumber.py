# 202. Happy Number 
class Solution:
    def isHappy(self, n: int) -> bool:
        new_n = 0
        n = str(n)
        used_set = set()

        while n!= 1:
            for i in str(n):
                square = int(i) ** 2 
                new_n += square
            
            if new_n not in used_set: 
                used_set.add(new_n)
            else:   
                return False
            n = new_n
            new_n = 0
        return n == 1