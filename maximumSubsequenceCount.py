# https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string/ 

class Solution(object):
	def maximumSubsequenceCount(self, text, pattern):
		def nsubseqs(text):
			res = 0
			count = 0
			for c in text:
				if c == pattern[1]:
					res += count

				if c == pattern[0]:
					count += 1

			return res

		return max(nsubseqs(pattern[0] + text), nsubseqs(text + pattern[1]))

"""
After I solve a problem, I like to study other people's solutions. I found a Java solution that uses the same idea as mine, but manages to do only 1 iteration:

https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string/discuss/1863892/First-or-Last

I have implemented the program in Python:
"""

class Solution(object):
	def maximumSubsequenceCount(self, text, pattern):
		N = len(text)

		count0, count1 = 1, 1
		res0, res1 = 0, 0
		j = N - 1
		for i in range(N):
			if text[i] == pattern[1]:
				res0 += count0

			if text[j] == pattern[0]:
				res1 += count1

			if text[i] == pattern[0]:
				count0 += 1

			if text[j] == pattern[1]:
				count1 += 1

			j -= 1

		return max(res0, res1)
