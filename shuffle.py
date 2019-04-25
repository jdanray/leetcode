# https://leetcode.com/problems/shuffle-an-array/

class Solution:
	def __init__(self, nums):
		self.orig = nums
		self.nums = nums

	def reset(self):
		self.nums = self.orig
		return self.nums

	def shuffle(self):
		self.nums = random.sample(self.nums, len(self.nums))
		return self.nums
