class Solution:
    def isValid(self, s: str) -> bool:
        op = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stack = []
        for c in s :
            if c in '({[' : stack.append(c)
            else :
                if not stack or stack[-1] != op[c] : return False
                stack.pop()
        return len(stack) == 0

        