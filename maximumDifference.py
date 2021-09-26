# https://leetcode.com/problems/maximum-difference-between-increasing-elements/ 

class Solution(object):
	def maximumDifference(self, nums):
		N = len(nums)

		res = -1
		for j in range(N):
			for i in range(j):
				d = nums[j] - nums[i]
				if d > 0:
					res = max(res, d)

		return res

"""
After I solve a problem, I like to examine other people's solutions. The following is O(n)-time:

https://leetcode.com/problems/maximum-difference-between-increasing-elements/discuss/1486309/SimIlar-to-Best-Time-to-Buy-and-Sell-StockC%2B%2B 

I implemented the same idea in Python:
"""

class Solution(object):
	def maximumDifference(self, nums):
		res = 0
		minPrice = float('inf')
		for n in nums:
			minPrice = min(minPrice, n)
			res = max(res, n - minPrice) 

		return res if res > 0 else -1
