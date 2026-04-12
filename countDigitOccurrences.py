# https://leetcode.com/problems/count-digit-appearances/

class Solution(object):
	def countDigitOccurrences(self, nums, digit):
		count = 0
		for n in nums:
			while n > 0:
				d = n % 10

				if d == digit:
					count += 1

				n //= 10

		return count