import unittest

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:  # Check for empty string
            return 0
        
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        
        for i in range(len(s) - 1):
            if roman_map[s[i]] < roman_map[s[i + 1]]:
                result -= roman_map[s[i]]  # Subtract if current is less than next
            else:
                result += roman_map[s[i]]  # Add if current is greater or equal

        result += roman_map[s[-1]]  # Add the last character's value
        return result