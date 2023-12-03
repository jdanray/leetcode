# https://leetcode.com/problems/count-beautiful-substrings-i/ 

class Solution(object):
	def beautifulSubstrings(self, s, k):
		vowels = 'aeiou'
		N = len(s)

		res = 0
		for i in range(N):
			count = [0, 0]
			for j in range(i, N):
				count[s[j] in vowels] += 1
				if count[0] == count[1] and (count[0] * count[1]) % k == 0:
					res += 1

		return res
