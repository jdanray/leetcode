# https://leetcode.com/problems/count-sorted-vowel-strings/

class Solution(object):
	def countVowelStrings(self, n):
		count = [1, 1, 1, 1, 1]
		for _ in range(n - 1):
			acc = 1
			for i in range(1, len(count)):
				acc += count[i]
				count[i] = acc

		return sum(count)
