# https://leetcode.com/problems/monotone-increasing-digits/ 

class Solution(object):
	def monotoneIncreasingDigits(self, n):
		original = n
		i = 0
		y = -1
		while n > 0 and (y == -1 or n % 10 <= y):
			i += 1
			y = n % 10
			n //= 10

		if y != -1 and n % 10 > y:
			start = (n // 10) * 10**(i + 1)
			mid = ((n % 10) - 1) * 10**i
			end = 10**i - 1
			return self.monotoneIncreasingDigits(start + mid + end)

		return original
