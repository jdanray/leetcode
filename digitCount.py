# https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/ 

class Solution(object):
	def digitCount(self, num):
		count = collections.Counter(num)
		return all(int(d) == count[str(i)] for i, d in enumerate(num))
