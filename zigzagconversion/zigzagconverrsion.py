# 6. Zigzag Conversion
# Medium
# Topics
# premium lock icon
# Companies
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);


# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:

# Input: s = "A", numRows = 1
# Output: "A"


# Constraints:

# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000


def oscilate(set_count, size):
    k = (set_count-1)*2
    # k = 2, c = 2
    # k = 4, c = 3
    # k = 6, c = 4
    # k = 8, c = 5
    # k = 10, c = 6
    l = int(k/2)
    for i in range(size):
        yield i, abs(((i-l) % k)-l)


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        size = len(s)
        matrix = []
        for r in range(numRows):
            matrix.append([])
        print(matrix)
        for i, row in oscilate(numRows, size):
            print(i, row)
            matrix[row].append(s[i])
        print(matrix)

        output = ''
        for row in matrix:
            output += ''.join(row)
        return output


sln = Solution()
o = sln.convert('abcdefghijklmnopqrstuv', 3)
print(o)
print(sln.convert('PAYPALISHIRING', 3))
print('PAHNAPLSIIGYIR')
print(sln.convert('PAYPALISHIRING', 4))
print('PINALSIGYAHRPI')
