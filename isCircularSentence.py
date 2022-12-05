# https://leetcode.com/problems/circular-sentence/ 

class Solution(object):
	def isCircularSentence(self, sentence):
		words = sentence.split()
		return all(words[i][-1] == words[i + 1][0] for i in range(len(words) - 1)) and words[-1][-1] == words[0][0]
