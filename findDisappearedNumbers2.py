# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array-ii/ 

class Solution(object):
	def findDisappearedNumbers(self, nums, lower, upper):
		nums = set(nums)
		res = []
		for n in range(lower, upper + 1):
			if n not in nums:
				if res and res[-1][-1] == n - 1:
					res[-1][-1] = n
				else:
					res.append([n, n])
		return res
