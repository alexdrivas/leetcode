class Solution:
    def canWinNim(self, n: int) -> bool:
        """
        n: int n > 0
        return bool: true if win the game or false: cannot win the game
        assume playing 'optimally'

        ex. 1
        n = 1 N < 3 6 through 3. 
        if n % 4 == 0, return false 
        if n % 6,5,3,2,1 == 0 return true
 
        """
        if n < 1:
            return "Not enough stones"
        
        if n % 4 == 0:
            return False 
        return True