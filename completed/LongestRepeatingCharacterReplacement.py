class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq = {}
        l = 0
        result = 0

        for r in range(len(s)):
            # 1. Add s[r] to freq dict
            freq[s[r]] = freq.get(s[r],0) + 1
            
            # 2. Check if window is valid 
            window_size = r - l + 1

            # 3. If invalid: remove s[l] from freq, move l forward
            if window_size - max(freq.values()) > k:
                freq[s[l]] -=1
                l +=1
            
            # 4. Update result with current window size (r - l + 1)
            result = max(result, r - l + 1)

        return result