# https://leetcode.com/problems/count-number-of-homogenous-substrings/

# sliding window (faster) 
class Solution(object):
	def countHomogenous(self, s):
		MOD = 10**9 + 7
		i = 0
		res = 0
		for j, c in enumerate(s):
			if s[i] != c:
				i = j

			res += (j - i + 1)

		return res % MOD

# sliding window 
class Solution(object):
	def countHomogenous(self, s):
		MOD = 10**9 + 7
		i = 0
		res = 0
		for j, c in enumerate(s):
			while s[i] != c:
				i += 1

			res += (j - i + 1)

		return res % MOD

class Solution(object):
	def countHomogenous(self, s):
		MOD = 10 ** 9 + 7
		N = len(s)
		i = 0
		res = 0
		while i < N:
			i += 1
			n = 1
			while i < N and s[i] == s[i - 1]:
				n += 1
				i += 1
			res += n * (n + 1) // 2
			res %= MOD
		return res

"""
After I solve a problem, I like to examine other people's solutions. Here is my Python implementation of the following idea:

https://leetcode.com/problems/count-number-of-homogenous-substrings/discuss/1064518/C%2B%2BJava-Simple-Counting
"""

class Solution(object):
	def countHomogenous(self, s):
		MOD = 10 ** 9 + 7
		res = 0
		for i, c in enumerate(s):
			if i > 0 and s[i - 1] == c:
				count += 1
			else:
				count = 1
			res += count
			res %= MOD
		return res
