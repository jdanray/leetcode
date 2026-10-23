# https://leetcode.com/problems/maximum-good-subarray-sum/

class Solution(object):
	def maximumSubarraySum(self, nums, k):
		s = 0
		sums = dict()
		res = 0
		for n in nums:
			s += n
			if n not in sums or sums[n] > s:
				sums[n] = s

			for d in [n - k, n + k]:
				if d in sums:
					x = s - sums[d] + d
					if res == 0 or x > res:
						res = x

		return res

class Solution(object):
	def maximumSubarraySum(self, nums, k):
		s = 0
		sums = dict()
		res = float('-inf')
		for n in nums:
			s += n
			if n not in sums or sums[n] > s:
				sums[n] = s

			if n - k in sums:
				res = max(res, s - sums[n - k] + n - k)

			if n + k in sums:
				res = max(res, s - sums[n + k] + n + k)

		return res if res != float('-inf') else 0