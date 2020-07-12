# https://leetcode.com/problems/number-of-substrings-with-only-1s/

class Solution(object):
	def numSub(self, s):
		MOD = 10**9 + 7
		count = 0
		res = 0
		for n in nums:
			if n == '1':
				count += 1
			else:
				count = 0

			res += count
			res %= MOD

		return  res
