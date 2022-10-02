# https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution(object):
	def equalFrequency(self, word):
		count = collections.Counter(word)
		for l in word:
			count[l] -= 1
			if len(count.values()) == 1:
				return True
			count[l] += 1

		return False
