# https://leetcode.com/problems/find-the-peaks/ 

class Solution(object):
	def findPeaks(self, m):
		return [i for i in range(1, len(m) - 1) if m[i - 1] < m[i] > m[i + 1]]
