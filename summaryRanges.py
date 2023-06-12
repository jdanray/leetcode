# https://leetcode.com/problems/summary-ranges/

class Solution(object):
	def summaryRanges(self, nums):
		res = []
		for i, n in enumerate(nums):
			if i - 1 >= 0 and n == nums[i - 1] + 1:
				if i + 1 == len(nums) or (i + 1 < len(nums) and n != nums[i + 1] - 1):
					res[-1] += '->' + str(n)
			else:
				res.append(str(n))
		return res

class Solution(object):
	def summaryRanges(self, nums):
		ranges = []
		for i, n in enumerate(nums):
			if i > 0 and nums[i - 1] == n - 1:
				ranges[-1][-1] = n
			else:
				ranges.append([n, n])

		return [str(u) if u == v else str(u) + '->' + str(v) for (u, v) in ranges]
