class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # if s = [], zero characters always true 
        # does a slice of our substring exist in the wordDict?
        # can we connect those slices from the beginning to the end? 
        
        if s is None: return True
        
        n = len(s) + 1 # init dp array as big s + 1 (for 0char condition)
        dp = [False]*n
        dp[0] = True 
         
        for i in range(n): # for each ch in wordDict
            for j in range(i): # for each between j and i  
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1] # if the last index of our substring is found in slice that is in wordDict