# https://leetcode.com/problems/check-if-the-sentence-is-pangram/

class Solution(object):
	def checkIfPangram(self, sentence):
		return len(set(sentence)) == 26
