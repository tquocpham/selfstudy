# 11. Container With Most Water
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.


# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1

class Solution(object):
    def maxArea(self, heights):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        for i in range(len(heights)):
            first = heights[i]
            for j in range(i+1, len(heights)):
                width = (j-i)
                second = heights[j]
                height = min(first, second)
                area = width * height
                if area > max_area:
                    max_area = area
        return max_area

    def maxAreaN(self, heights):
        L = 0
        R = len(heights) - 1
        max_vol = 0
        while L != R:
            width = R-L
            height = min(heights[L], heights[R])
            vol = width * height
            if vol > max_vol:
                max_vol = vol
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1

        return max_vol


sln = Solution()
assert 49 == sln.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
assert 6 == sln.maxArea([0, 8, 6, 1, 1, 1, 1, 1])
assert 7 == sln.maxArea([0, 8, 6, 1, 1, 1, 1, 1, 1])
assert 1 == sln.maxArea([1, 1])

assert 49 == sln.maxAreaN([1, 8, 6, 2, 5, 4, 8, 3, 7])
assert 6 == sln.maxAreaN([0, 8, 6, 1, 1, 1, 1, 1])
assert 7 == sln.maxAreaN([0, 8, 6, 1, 1, 1, 1, 1, 1])
assert 1 == sln.maxAreaN([1, 1])
