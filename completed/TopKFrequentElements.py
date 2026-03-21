class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # construct frequency dict {value, frequency}
        d = {}
        output = []
        max_n = 0

        for i in nums:
            d[i] = d.get(i,0) + 1 # get(key, default)
        print(d)

        # sort the dict 
        s = sorted(d.items(), key=lambda x: x[1], reverse = True)

        output = s[:k]
        result = []
        for i in output:
            result.append(i[0])
        return result