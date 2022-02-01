# https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/ 

class Solution(object):
	def maxScoreIndices(self, nums):
		zeros = 0
		ones = sum(nums)
		maxim = ones
		res = [0]
		for i, n in enumerate(nums):
			if n == 0:
				zeros += 1
			else:
				ones -= 1

			s = zeros + ones
			if s > maxim:
				res = [i + 1]
				maxim = s
			elif s == maxim:
				res.append(i + 1)

		return res
