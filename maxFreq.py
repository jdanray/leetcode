# https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/

class Solution(object):
	def maxFreq(self, s, maxLetters, minSize, maxSize):
		count = collections.Counter()
		for i in range(len(s)):
			sub = ""
			chars = set()
			nunique = 0
			for j in range(i, i + maxSize):
				if j >= len(s):
					continue

				sub += s[j]
				nunique += 1

				if s[j] in chars:
					nunique -= 1

				if len(sub) >= minSize and nunique <= maxLetters:
					count[sub] += 1

				chars.add(s[j])

		return max(count.values()) if count else 0

class Solution(object):
	def maxFreq(self, s, maxLetters, minSize, maxSize):
		i = 0
		res = 0
		uniques = 0
		seenChars = collections.Counter()
		countSubs = collections.Counter()
		for j, c in enumerate(s):
			if seenChars[c] == 0:
				uniques += 1
			seenChars[c] += 1

			while uniques > maxLetters or j - i + 1 > minSize:
				seenChars[s[i]] -= 1
				if seenChars[s[i]] == 0:
					uniques -= 1
				i += 1

			if j - i + 1 == minSize:
				sub = s[i:j + 1]
				countSubs[sub] += 1
				res = max(res, countSubs[sub])

		return res
