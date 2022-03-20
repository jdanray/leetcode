# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/ 

class Solution(object):
	def findKDistantIndices(self, nums, key, k):
		indexes = [i for i, n in enumerate(nums) if n == key]
		j = 0
		res = []
		for i in range(len(nums)):
			if j < len(indexes) and i > indexes[j] + k:
				j += 1

			if j < len(indexes) and indexes[j] - k <= i <= indexes[j] + k:
				res.append(i)

		return res

class Solution(object):
	def findKDistantIndices(self, nums, key, k):
		N = len(nums)

		res = set()
		for i, n in enumerate(nums):
			if n != key:
				continue

			for j in range(k + 1):
				if i - j >= 0:
					res.add(i - j)

				if i + j < N:
					res.add(i + j)

		return sorted(res)
