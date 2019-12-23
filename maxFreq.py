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
