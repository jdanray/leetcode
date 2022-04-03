# https://leetcode.com/problems/number-of-ways-to-select-buildings/

class Solution(object):
	def numberOfWays(self, s):
		count = collections.Counter()
		res = 0
		for c in s:
			count[c] += 1

			if c == '1':
				res += count['10']
				count['01'] += count['0']
			else:
				res += count['01']
				count['10'] += count['1']

		return res
