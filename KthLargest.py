# https://leetcode.com/problems/kth-largest-element-in-a-stream/ 

class KthLargest(object):
	def __init__(self, k, nums):
		self.k = k
		self.nums = nums

	def add(self, val):
		self.nums.append(val)
		self.nums = sorted(self.nums)
		return self.nums[len(self.nums) - self.k]
