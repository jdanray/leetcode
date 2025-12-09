# https://leetcode.com/problems/count-special-triplets/

class Solution(object):
	def specialTriplets(self, nums):
		MOD = 10**9 + 7

		left = collections.Counter()
		right = collections.Counter(nums)
		res = 0
		for n in nums:
			right[n] -= 1
			res += left[n * 2] * right[n * 2]
			left[n] += 1

		return res % MOD