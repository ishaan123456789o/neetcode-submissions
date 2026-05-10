class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            elif ch == ')':
                if len(stack) == 0 or stack[-1] != '(':
                    return False
                stack.pop()
            elif ch == '}':
                if len(stack) == 0 or stack[-1] != '{':
                    return False
                stack.pop()
            elif ch == ']':
                if len(stack) == 0 or stack[-1] != '[':
                    return False
                stack.pop()
        if len(stack) == 0:
            return True
        return False
        