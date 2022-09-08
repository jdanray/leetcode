# https://leetcode.com/problems/strictly-palindromic-number/ 

class Solution(object):
	def isStrictlyPalindromic(self, n):
		for b in range(2, n - 1):
			m = n
			num = []
			while m > 0:
				num.append(m % b)
				m //= b

			i = 0
			j = len(num) - 1
			while i < j and num[i] == num[j]:
				i += 1
				j -= 1

			if i < j:
				return False

		return True
