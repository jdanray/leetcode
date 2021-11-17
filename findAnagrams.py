# https://leetcode.com/problems/find-all-anagrams-in-a-string/

from collections import Counter

class Solution:
	def findAnagrams(self, s, p):
		if len(s) < len(p):
			return []

		pcount = Counter(p)
		scount = Counter(s[:len(p) - 1])

		indices = []
		for i in range(len(s) - len(p) + 1):
			scount[s[i + len(p) - 1]] += 1

			if scount == pcount:
				indices.append(i)

			scount[s[i]] -= 1
			if scount[s[i]] == 0:
				del scount[s[i]]

		return indices

class Solution(object):
	def findAnagrams(self, s, p):
		countAnagram = collections.Counter(p)
		countChars = collections.Counter()
		i = 0
		res = []
		for j, c in enumerate(s):
			countChars[c] += 1

			while any(countChars[x] > countAnagram[x] for x in countChars):
				countChars[s[i]] -= 1
				if countChars[s[i]] == 0: 
					del countChars[s[i]]
				i += 1

			if countChars == countAnagram:
				res.append(i)

		return res
