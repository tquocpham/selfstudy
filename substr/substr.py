
# Code


# Testcase
# Test Result
# Test Result
# 3. Longest Substring Without Repeating Characters
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given a string s, find the length of the longest substring without duplicate characters.


# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        counters = {}
        substrs = []
        substrbuilder = ''
        for char in s:
            if char in counters:
                substrs.append(substrbuilder[:])
                counters = {}
                substrbuilder = ''
            counters[char] = True
            substrbuilder += char

        # final
        substrs.append(substrbuilder[:])

        max_len = 0
        for substr in substrs:
            if len(substr) > max_len:
                max_len = len(substr)

        print(substrs)
        return max_len


sln = Solution()
print(sln.lengthOfLongestSubstring("abcabcbb"))
print(sln.lengthOfLongestSubstring("bbbbbb"))
print(sln.lengthOfLongestSubstring("pwwkew"))
