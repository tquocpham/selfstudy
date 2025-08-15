
# Code
# Testcase
# Test Result
# Test Result
# 1. Two Sum
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

# Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return i, j
        return None

    def twoSumPartB(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}
        for i, n in enumerate(nums):
            comp = target - n
            if comp in num_map:
                return (i, num_map[comp])
            num_map[n] = i


sln = Solution()
print(sln.twoSum([2, 7, 11, 15], 9))
print(sln.twoSumPartB([2, 7, 11, 15], 9))
print(sln.twoSum([3, 2, 4], 6))
print(sln.twoSumPartB([3, 2, 4], 6))
