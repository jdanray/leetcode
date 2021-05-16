# https://leetcode.com/problems/sorting-the-sentence/ 

class Solution(object):
	def sortSentence(self, s):
		s = s.split()
		s = sorted(s, key=lambda w: int(w[-1]))
		s = " ".join(w[:-1] for w in s)
		return s
