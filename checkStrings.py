# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/ 

class Solution(object):
	def checkStrings(self, s1, s2):
		odd1 = collections.Counter(s1[i] for i in range(0, len(s1), 2))
		odd2 = collections.Counter(s2[i] for i in range(0, len(s2), 2))

		even1 = collections.Counter(s1[i] for i in range(1, len(s1), 2))
		even2 = collections.Counter(s2[i] for i in range(1, len(s2), 2))

		return odd1 == odd2 and even1 == even2
