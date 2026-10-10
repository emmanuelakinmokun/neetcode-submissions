class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairings = {'}': '{', ')' :'(', ']':'[' }
        for c in s:
            if c in pairings:
                if stack and stack[-1] == pairings[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
        
