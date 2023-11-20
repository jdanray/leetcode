# https://leetcode.com/problems/make-three-strings-equal/ 

class Solution(object):
	def findMinimumOperations(self, s1, s2, s3):
		if s1[0] != s2[0] or s1[0] != s3[0]:
			return -1

		i = 0
		j = 0
		k = 0
		while i < len(s1) and j < len(s2) and k < len(s3) and s1[i] == s2[j] == s3[k]:
			i += 1
			j += 1
			k += 1

		return (len(s1) - i) + (len(s2) - j) + (len(s3) - k)
