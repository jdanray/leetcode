# https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/ 

class Solution(object):
	def minimumOperations(self, nums):
		pos = [n for n in nums if n > 0]

		if not pos:
			return 0

		m = min(pos)
		return 1 + self.minimumOperations([p - m for p in pos])

class Solution(object):
	def minimumOperations(self, nums):
		res = 0
		nums = [n for n in nums if n > 0]
		while nums:
			res += 1
			m = min(nums)
			nums = [n - m for n in nums if n > m]
            
		return res
