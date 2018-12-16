# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

class Solution(object):
	def nextGreatestLetter(self, letters, target):
		if target >= letters[-1]:
			return letters[0]

		i = 0
		while target >= letters[i]:
			i += 1
		return letters[j]
