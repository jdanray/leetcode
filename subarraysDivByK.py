# https://leetcode.com/problems/subarray-sums-divisible-by-k/ 

class Solution(object):
	def subarraysDivByK(self, nums, k):
		count = collections.Counter()
		count[0] = 1
		s = 0
		res = 0
		for n in nums:
			s = (s + n) % k
			res += count[s]
			count[s] += 1

		return res
