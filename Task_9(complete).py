"""
Given an integer x, return true if x is a palindrome, and false otherwise.
Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""


class Solution:
    def ispalindrome(self, x: int) -> bool:
        digit_list = []
        if x > -1:
            while x > 0:
                ld = x % 10
                x = x//10
                digit_list.append(ld)
            if digit_list[::-1] == digit_list:
                return True
            else:
                return False
        else:
            return False
