import unittest

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            elif char in bracket_map.keys():
                if not stack or stack.pop() != bracket_map[char]:
                    return False

        return not stack
    
solution = Solution()
print(solution.isValid("()"))  
print(solution.isValid("()[]{}"))  
print(solution.isValid("{[()]}"))  
