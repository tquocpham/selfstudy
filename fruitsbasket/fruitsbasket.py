
# Code
# Testcase
# Test Result
# Test Result
# 2561. Rearranging Fruits
# Hard
# Topics
# premium lock icon
# Companies
# Hint
# You have two fruit baskets containing n fruits each. You are given two 0-indexed integer arrays basket1 and basket2 representing the cost of fruit in each basket. You want to make both baskets equal. To do so, you can use the following operation as many times as you want:

# Chose two indices i and j, and swap the ith fruit of basket1 with the jth fruit of basket2.
# The cost of the swap is min(basket1[i],basket2[j]).
# Two baskets are considered equal if sorting them according to the fruit cost makes them exactly the same baskets.

# Return the minimum cost to make both the baskets equal or -1 if impossible.


# Example 1:

# Input: basket1 = [4,2,2,2], basket2 = [1,4,1,2]
# Output: 1
# Explanation: Swap index 1 of basket1 with index 0 of basket2, which has cost 1. Now basket1 = [4,1,2,2] and basket2 = [2,4,1,2]. Rearranging both the arrays makes them equal.
# Example 2:

# Input: basket1 = [2,3,4,1], basket2 = [3,2,5,1]
# Output: -1
# Explanation: It can be shown that it is impossible to make both the baskets equal.


# [3, 3, 4, 4, 5, 5, 7, 8, 9] {1: 0, 3: 2, 4: 2, 5: 2, 6: 0, 7: 1, 8: 1, 9: 1}
# [1, 1, 1, 1, 6, 6, 7, 8, 9] {1: 4, 3: 0, 4: 0, 5: 0, 6: 2, 7: 1, 8: 1, 9: 1}

# trade 3a for 6b (cost 3)
# [3, 4, 4, 5, 5, 6, 7, 8, 9] {1: 0, 3: 1, 4: 2, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
# [1, 1, 1, 1, 3, 6, 7, 8, 9] {1: 4, 3: 1, 4: 0, 5: 0, 6: 1, 7: 1, 8: 1, 9: 1}

# trade 4a for 1b (cost 1)
# [1, 3, 4, 5, 5, 6, 7, 8, 9] {1: 1, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
# [1, 1, 1, 3, 4, 6, 7, 8, 9] {1: 3, 3: 1, 4: 1, 5: 0, 6: 1, 7: 1, 8: 1, 9: 1}

# trade 5a for 1b (cost 1)
# [1, 1, 3, 4, 5, 6, 7, 8, 9] {1: 2, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}
# [1, 1, 3, 4, 5, 6, 7, 8, 9] {1: 2, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}


# [2,3,4,1] {1:1, 2:1, 3:1, 4:0, 5:1}
# [3,2,5,1] {1:1, 2:1, 3:1, 4:1, 5:1}
from typing import List


class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        # check that all counts sbetween the baskets are even.
        # if odd, there's no way both basketss can have the same
        # number
        allcounts = {}
        for b in basket1:
            if b not in allcounts:
                allcounts[b] = 0
            allcounts[b] += 1
        for b in basket2:
            if b not in allcounts:
                allcounts[b] = 0
            allcounts[b] += 1
        for d, c, in allcounts.items():
            if c % 2 != 0:
                return -1
        total_cost = 0
        while True:
            b1Count = self.count(basket1, allcounts.keys())
            b2Count = self.count(basket2, allcounts.keys())
            if self.are_counts_equal(b1Count, b2Count):
                break

            # find largest deficet
            max_def = 0
            min_surp = None
            print(basket1)
            print(basket2)
            for d, c in b1Count.items():
                b2c = 0
                if d in b2Count:
                    b2c = b2Count[d]
                print(d, c, b2c, max_def, min_surp)
                if b2c > c and d > max_def:
                    max_def = d
                if c > b2c:
                    if min_surp is None:
                        min_surp = d
                    if d < min_surp:
                        min_surp = d
            print(max_def, min_surp)
            cost = min(max_def, min_surp)
            total_cost += cost

            print(f'trading {max_def} for {min_surp} cost {cost}')
            self.trade(max_def, min_surp, basket1, basket2)

    def count(self, basket, digits):
        counts = {d: 0 for d in digits}
        for b in basket:
            counts[b] += 1
        return counts

    def are_counts_equal(self, count1, count2):
        for d, c in count1.items():
            if c != count2[d]:
                return False
        return True

    def trade(self, buy, sell, buyerbasket, sellerbasket):
        buyerbasket.remove(sell)
        sellerbasket.append(sell)
        sellerbasket.remove(buy)
        buyerbasket.append(buy)


sln = Solution()
b1 = [3, 3, 4, 4, 5, 5, 7, 8, 9]
b2 = [1, 1, 1, 1, 6, 6, 7, 8, 9]
sln.minCost(b1, b2)
