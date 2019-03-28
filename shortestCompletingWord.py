# https://leetcode.com/problems/shortest-completing-word/ 

from collections import Counter

class Solution:
	def shortestCompletingWord(self, licensePlate, words):
		countlic = Counter(c.lower() for c in licensePlate if c.isalpha())
		completer = None
		for w in words:
			countword = Counter(w)
			if any(c not in countword or countword[c] < countlic[c] for c in countlic):
				continue
			
			if completer == None or len(w) < len(completer):
				completer = w

		return completer
