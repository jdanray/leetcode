# https://leetcode.com/problems/count-number-of-homogenous-substrings/

"""
N=1
'a' appears once

N=2
'a' appears twice
'aa' appears once

N=3
'a' appears thrice
'aa' appears twice
'aaa' appears once

N=4
'a' appears four times
'aa' appears three times
'aaa' appears twice 
'aaaa' appears once
"""

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
