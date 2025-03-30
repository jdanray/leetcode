# https://leetcode.com/problems/maximize-active-section-with-trade-i/

class Solution(object):
	def maxActiveSectionsAfterTrade(self, s):
		ones = 0
		left = 0
		right = 0
		flip = 0
		for b in s:
			if b == '1':
				ones += 1
				if right > 0:
					left = right
					right = 0
			elif b == '0':
				right += 1
				if left > 0:
					flip = max(flip, left + right)

		return flip + ones