# https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/ 

class Solution(object):
	def averageValue(self, nums):
		cands = [n for n in nums if n % 2 == 0 and n % 3 == 0]

		if not cands:
			return 0
		else:
			return int(math.floor(1.0 * sum(cands) / len(cands)))
