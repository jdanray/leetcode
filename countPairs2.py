# https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/ 

class Solution(object):
	def countPairs(self, nums, k):
		return sum(1 if nums[i] == nums[j] and (i * j) % k == 0 else 0 for j in range(len(nums)) for i in range(j))
