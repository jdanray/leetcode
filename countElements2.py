# https://leetcode.com/problems/count-elements-with-at-least-k-greater-values/

class Solution(object):
	def countElements(self, nums, k):
		l = len(nums)

		count = collections.Counter(nums)
		keys = sorted(count.keys())

		s = 0
		res = 0
		for n in keys:
			s += count[n]
			if l - s >= k:
				res += count[n]

		return res

class Solution(object):
	def countElements(self, nums, k):
		N = len(nums)

		nums = sorted(nums)
		i = 0
		res = 0
		while i < N:
			s = 1
			while i + 1 < N and nums[i] == nums[i + 1]:
				s += 1
				i += 1

			if N - i - 1 >= k:
				res += s

			i += 1

		return res