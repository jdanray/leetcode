# https://leetcode.com/problems/find-the-k-or-of-an-array/

class Solution(object):
	def findKOr(self, nums, k):
		M = 32

		res = 0
		for b in range(M):
			count = 0
			for i in range(len(nums)):
				count += (nums[i] & 1)
				nums[i] >>= 1

			if count >= k:
				res += (1 << b)

		return res

class Solution(object):
	def findKOr(self, nums, k):
		count = collections.Counter()
		for n in nums:
			b = 0
			while n > 0:
				count[b] += (n & 1)
				b += 1
				n >>= 1

		res = 0
		for b in count:
			if count[b] >= k:
				res += (1 << b)

		return res
