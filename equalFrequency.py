# https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution(object):
	def equalFrequency(self, word):
		count = collections.Counter(word)
		for c in word:
			count[c] -= 1
			l = len(set(count.values()))
			if l == 1 or (l == 2 and count[c] == 0):
				return True
			count[c] += 1
            
		return False
