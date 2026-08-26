class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')':'(', '}':'{', ']':'['}
        stk = []
        for c in s:
            if c in pairs:
                if stk and stk[-1] == pairs[c]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c)
        return True if not stk else False