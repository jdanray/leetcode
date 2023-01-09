# https://leetcode.com/problems/make-number-of-distinct-characters-equal/

class Solution(object):
	def isItPossible(self, word1, word2):
		ndc1 = len(set(word1))
		ndc2 = len(set(word2))

		count1 = collections.Counter(word1)
		count2 = collections.Counter(word2)

		for c1 in count1:
			for c2 in count2:
				n1 = ndc1
				n2 = ndc2

				if count1[c1] == 1:
					n1 -= 1
				if count1[c2] == 0 or (c1 == c2 and count1[c2] == 1):
					n1 += 1

				if count2[c2] == 1:
					n2 -= 1
				if count2[c1] == 0 or (c1 == c2 and count2[c1] == 1):
					n2 += 1

				if n1 == n2:
					return True

		return False
