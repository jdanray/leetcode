# https://leetcode.com/problems/special-array-ii/ 

class Solution(object):
	def isArraySpecial(self, nums, queries):
		N = len(nums)

		spec = [0 for _ in range(N)] 
		s = 0
		for i in range(1, N):
			if nums[i] % 2 == nums[i - 1] % 2:
				s = 0
			else:
				s += 1

			spec[i] = s

		return [j - spec[j] <= i for (i, j) in queries]
