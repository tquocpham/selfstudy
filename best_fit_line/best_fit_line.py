from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        max_pts_on_line = 0
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]

                if x2 == x1:
                    continue

                slope = (y2 - y1)/(x2 - x1)
                intercept = y1 - (slope * x1)

                pts_on_line = 0
                for c in points:
                    xc, yc = c
                    if (slope * xc + intercept) == yc:
                        pts_on_line += 1
                if pts_on_line > max_pts_on_line:
                    max_pts_on_line = pts_on_line
        return max_pts_on_line


points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
sln = Solution()
print(sln.maxPoints(points))
points = [[1, 1], [2, 2], [3, 3]]
print(sln.maxPoints(points))
