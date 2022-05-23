# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/ 

class Solution(object):
	def removeAnagrams(self, words):
		stack = [words[0]]
		for w in words:
			if collections.Counter(w) != collections.Counter(stack[-1]):
				stack.append(w)
		return stack
