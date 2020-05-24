# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

class Solution(object):
	def isPrefixOfWord(self, sentence, searchWord):
		N = len(searchWord)
		for i, word in enumerate(sentence.split()):
			if len(word) >= N and word[:N] == searchWord: 
				return i + 1
            
		return -1
