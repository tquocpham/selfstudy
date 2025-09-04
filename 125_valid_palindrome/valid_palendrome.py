# 125. Valid Palindrome
# Easy
# Topics
# premium lock icon
# Companies
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.


# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.


# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        valid_chars = 'abcdefghijklmnopqrstuvwxyz'
        s = s.lower()
        for c in s:
            if c not in valid_chars:
                s = s.replace(c, '')

        letters = int(len(s)/2)
        for i in range(letters):
            c1 = s[i]
            c2 = s[len(s)-1-i]
            if c1 != c2:
                return False
        return True


sln = Solution()
print(sln.isPalindrome("race a car"))
