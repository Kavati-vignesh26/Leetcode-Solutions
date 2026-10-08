class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        d = 0
        for c in s:
            d += 1 if c == '(' else -1
            if (c == '(' and d == 1) or (c == ')' and d == 0): continue
            res.append(c)
        return  "".join(res)
        