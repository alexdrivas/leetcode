class Solution:
    def maxProduct(self, words: List[str]) -> int:
        print(sorted(words, key = lambda x: len(x), reverse=True))

        lookup = defaultdict(set)

        for w in words: # key is the wole word, value is the set
            lookup[w] = set(w)
        
        def dont_share(s,t):
            if lookup[s]&lookup[t]:
                return False
            return True
        
        mx = 0
        for i in words:
            for j in words:
                if dont_share(i,j):
                    mx = max(mx,len(i)*len(j))
        return mx
