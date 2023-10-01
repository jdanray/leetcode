# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/ 

class Solution(object):
	def maximumTripletValue(self, nums):
		N = len(nums)

		res = 0
		for k in range(N):
			for j in range(k):
				for i in range(j):
					res = max(res, (nums[i] - nums[j]) * nums[k])

		return res

class Solution(object):
	def maximumTripletValue(self, nums):
		N = len(nums)

		d = collections.defaultdict(int)
		for j in range(N):
			for i in range(j):
				d[j] = max(d[j], nums[i] - nums[j])

		res = 0
		for k in range(N):
			for j in range(k):
				res = max(res, d[j] * nums[k])

		return res
