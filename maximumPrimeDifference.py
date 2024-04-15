# https://leetcode.com/problems/maximum-prime-difference/

class Solution(object):
	def maximumPrimeDifference(self, nums):
		primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}

		start = -1
		res = 0
		for i, n in enumerate(nums):
			if n in primes:
				if start == -1:
					start = i

				res = max(res, i - start)

		return res
