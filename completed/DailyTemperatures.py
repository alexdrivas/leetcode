class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        stack = [] # [temperature, index]

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]: # temp is greater than stack temp
                stackTemp, stackInd = stack.pop()
                res[stackInd] = i - stackInd # we want the number of steps between indicies
            stack.append([t, i]) 
        return res