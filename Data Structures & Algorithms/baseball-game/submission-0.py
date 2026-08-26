class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # + = (i-1) + (i-2)
        # D = 2(i-1)
        # C = remove prev score
        stk = []
        for ops in operations:
            if ops == "+":
                stk.append(stk[-1] + stk[-2])

            elif ops == "D":
                stk.append(stk[-1] * 2)

            elif ops == "C":
                stk.pop()
            else: 
                stk.append(int(ops))
        return sum(stk)    