# https://leetcode.com/problems/find-the-maximum-divisibility-score/ 

class Solution(object):
	def maxDivScore(self, nums, divisors):
		score = [divisors[0], 0]
		for d in divisors:
			s = 0
			for n in nums:
				if n % d == 0:
					s += 1

			if s > score[1] or (s == score[1] and d < score[0]):
				score = [d, s]
            
		return score[0]
