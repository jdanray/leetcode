# https://leetcode.com/problems/truncate-sentence/ 

class Solution(object):
	def truncateSentence(self, s, k):
		return " ".join(s.split()[:k])
