# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/ 

class Solution(object):
	def divideArray(self, nums, k):
		N = 3

		if len(nums) % N != 0:
			return []

		heapq.heapify(nums)
		res = []
		while len(nums) >= N:
			abc = []
			for _ in range(N):
				n = heapq.heappop(nums)
				abc.append(n)

			if abc[-1] - abc[0] > k:
				return []

			res.append(abc)

		return res

class Solution(object):
	def divideArray(self, nums, k):
		if len(nums) % 3 != 0:
			return []

		heapq.heapify(nums)
		res = []
		while len(nums) >= 3:
			a = heapq.heappop(nums)
			b = heapq.heappop(nums)
			c = heapq.heappop(nums)

			if c - a > k:
				return []

			res.append([a, b, c])

		return res

class Solution(object):
	def divideArray(self, nums, k):
		nums = sorted(nums)
		res = []
		for i in range(0, len(nums), 3):
			if nums[i + 2] - nums[i] > k:
				return []
			else:
				res.append([nums[i], nums[i + 1], nums[i + 2])
		return res 
