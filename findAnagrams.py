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

class Solution:
	def findAnagrams(self, s, p):
		N = len(p)

		countAnagram = collections.Counter(p)
		countChars = collections.Counter()

		res = []
		# Invariant: countChars stores the char count for s[i-len(p)+1..i], for 0 <= i < len(s)
		for i, c in enumerate(s):
			countChars[c] += 1

			if i >= N:
				first = s[i - N]
				countChars[first] -= 1
				if countChars[first] == 0:
					del countChars[first]

			if countChars == countAnagram:
				res.append(i - N + 1)

		return res
