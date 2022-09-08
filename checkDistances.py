# https://leetcode.com/problems/check-distances-between-same-letters/ 

class Solution(object):
	def checkDistances(self, s, distance):
		N = len(s)
		alphabet = string.ascii_lowercase
		d = {c: distance[i] for i, c in enumerate(alphabet)}
		return all((i + d[c] + 1 < N and s[i + d[c] + 1] == c) or (i - d[c] - 1 >= 0 and s[i - d[c] - 1] == c) for i, c in enumerate(s))
