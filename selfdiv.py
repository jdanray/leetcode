# https://leetcode.com/problems/self-dividing-numbers/description/ 

class Solution:
	def divides(self, num):
		n = int(num)
		while n > 0:
			m = n % 10
			if m == 0 or num % m != 0:
				return False		
			n //= 10
		return True

	def selfDividingNumbers(self, left, right):
		return [num for num in range(left, right + 1) if self.divides(num)]
		
