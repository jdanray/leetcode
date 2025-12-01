# https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/

class Solution(object):
	def minMirrorPairDistance(self, nums):
		def reverse(num):
			res = 0
			while num > 0:
				res *= 10
				res += (num % 10)
				num //= 10
			return res

		seen = dict()
		res = float('inf')
		for j, n in enumerate(nums):
			if n in seen:
				res = min(res, j - seen[n])

			seen[reverse(n)] = j

		return res if res != float('inf') else -1