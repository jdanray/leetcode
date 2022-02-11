# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/

class Solution(object):
	def minimumSum(self, num):
		digits = []
		while num > 0:
			digits.append(num % 10)
			num //= 10

		digits = sorted(digits)
		return (10 * digits[0] + digits[2]) + (10 * digits[1] + digits[3])
