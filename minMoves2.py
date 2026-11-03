# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/

class Solution(object):
	def minMoves(self, nums):
		m = max(nums)
		return sum(m - n for n in nums)

class Solution(object):
	def minMoves(self, nums):
		mx = nums[0]
		res = 0
		for i in range(1, len(nums)):
			n = nums[i]
			if n > mx:
				res += i * (n - mx)
				mx = n
			else:
				res += mx - n

		return res
