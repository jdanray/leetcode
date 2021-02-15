# https://leetcode.com/problems/tuple-with-same-product/

"""
The evolution of an idea:
"""

class Solution(object):
	def tupleSameProduct(self, nums):
		count = {}
		for i, x in enumerate(nums):
			for j, y in enumerate(nums):
				if i == j:
					continue

				p = x * y
				if p in count:
					n, used = count[p]
					if not (x in used or y in used):
						count[p] = (n + 1, used | {x, y})
				else:
					count[p] = (1, {x, y})

		res = 0
		for p in count:
			n, _ = count[p]
			for i in range(n):
				res += i * 8
		return res

class Solution(object):
	def tupleSameProduct(self, nums):
		count = {}
		res = 0
		for i, x in enumerate(nums):
			for j, y in enumerate(nums):
				if i == j:
					continue

				p = x * y
				if p in count:
					n, used = count[p]
					if not (x in used or y in used):
						count[p] = (n + 1, used | {x, y})
						res += n * 8
				else:
					count[p] = (1, {x, y})
		return res

class Solution(object):
	def tupleSameProduct(self, nums):
		count = {}
		res = 0
		for i, x in enumerate(nums):
			for j in range(i + 1, len(nums)):
				y = nums[j]
				p = x * y
				if p in count:
					n, used = count[p]
					if not (x in used or y in used):
						count[p] = (n + 1, used | {x, y})
						res += n * 8
				else:
					count[p] = (1, {x, y})
		return res

class Solution(object):
	def tupleSameProduct(self, nums):
		N = len(nums)
		count = {}
		res = 0
		for i in range(N):
			for j in range(i + 1, N):
				p = nums[i] * nums[j]
				if p in count:
					res += count[p] * 8
					count[p] += 1 
				else:
					count[p] = 1
		return res
