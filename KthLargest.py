# https://leetcode.com/problems/kth-largest-element-in-a-stream/ 

class KthLargest(object):
	def __init__(self, k, nums):
		self.k = k
		self.nums = nums

	def add(self, val):
		self.nums.append(val)
		self.nums = sorted(self.nums)
		return self.nums[len(self.nums) - self.k]

from sortedcontainers import SortedList

class KthLargest(object):
	def __init__(self, k, nums):
		self.k = k
		self.elems = SortedList()
		for n in nums:
			self.elems.add(n)

	def add(self, val):
		self.elems.add(val)
		return self.elems[-self.k]
