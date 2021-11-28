# https://leetcode.com/problems/count-common-words-with-one-occurrence/ 

class Solution(object):
	def countWords(self, words1, words2):
		count1 = collections.Counter(words1)
		count2 = collections.Counter(words2)

		res = 0
		for w in count1:
			if count1[w] == 1 and count2[w] == 1:
				res += 1

		return res
