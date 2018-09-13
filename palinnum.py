# https://leetcode.com/problems/palindrome-number/description/

class Solution(object):
	def isPalindrome(self, x):
		if x < 0:
			return False

		l = 0
		n = int(x)
		while n > 0:
			l += 1
			n //= 10

		s = []
		i = 0
		k = l // 2
		while x > 0:
			d = x % 10
			if i < k:
				s.append(d)
			elif not (i == k and l % 2 == 1):
				u = s.pop()
				if u != d:
					return False
			i += 1
			x //= 10
		return True
