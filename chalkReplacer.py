# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/

class Solution(object):
	def chalkReplacer(self, chalk, k):
		s = sum(chalk)
		r = k % s
		for i, c in enumerate(chalk):
			if c > r:
				return i
			else:
				r -= c
		return 0
