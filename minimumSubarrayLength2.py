# https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/ 

class Solution(object):
	def minimumSubarrayLength(self, nums, k):
		B = 32

		def getOR(count):
			res = 0
			for b in count:
				if count[b] > 0:
					res |= (1 << b)
			return res

		def addOR(n, count):
			for b in range(B):
				if (n >> b) & 1 == 1:
					count[b] += 1

		def removeOR(n, count):
			for b in range(B):
				if (nums[i] >> b) & 1 == 1:
					count[b] -= 1

		i = 0
		count = collections.Counter()
		res = float('inf')
		for j, n in enumerate(nums):
			addOR(n, count)
			while i <= j and getOR(count) >= k:
				res = min(res, j - i + 1)
				removeOR(n, count)
				i += 1

		return -1 if res == float('inf') else res
