class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [0] * len(temperatures)
    
    # [28, 40, 35, 36, 30, 38, 30] (top to bottom)

        for i in range(len(temperatures)):
            while stk and temperatures[i] > temperatures[stk[-1]]:
                prev = stk.pop()
                res[prev] = i - prev
            stk.append(i)
        return res
