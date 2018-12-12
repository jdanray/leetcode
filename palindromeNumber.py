# https://leetcode.com/problems/palindrome-number/

class Solution(object):
	def isPalindrome(self, x):
		if x < 0:
			return False
		elif x == 0:
			return True

		digs = []
		while x > 0:
			digs.append(x % 10)
			x //= 10

		i = 0
		j = len(digs) - 1
		while i < j:
			if digs[i] != digs[j]:
				return False
			else:
				i += 1
				j -= 1

		return True

class Solution(object):
	def isPalindrome(self, x):
		x = str(x)
		if not x or x[0] == '-':
			return False
		s = 0
		f = len(x) - 1
		for _ in range(len(x) // 2):
			if x[s] != x[f]:
				return False
			s += 1
			f -= 1
		return True

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
