# https://leetcode.com/problems/plus-one/description/

class Solution:
	def plusOne(self, digits):
		carry = 1
		for i in range(len(digits), -1, -1):
			s = digits[i] + carry
			digits[i] = s % 10
			carry = s // 10
		if carry:
			digits = [carry] + digits
		return digits
