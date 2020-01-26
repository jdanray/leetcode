# https://leetcode.com/problems/print-words-vertically/ 

class Solution(object):
	def printVertically(self, s):
		s = s.split()
		M = max(len(word) for word in s)
		res = [""] * M
		for word in s:
			for i in range(M):
				if i < len(word):
					res[i] += word[i]
				else:
					res[i] += " "
                    
		return [chars.rstrip() for chars in res]
