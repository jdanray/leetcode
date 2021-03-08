# https://leetcode.com/problems/sum-of-beauty-of-all-substrings/ 

class Solution(object):
	def beautySum(self, s):
		N = len(s)
		res = 0
		for i in range(N):
			count = collections.Counter()
			for j in range(i, N):
				count[s[j]] += 1
				res += (max(count.values()) - min(count.values()))
		return res
