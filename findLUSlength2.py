# https://leetcode.com/problems/longest-uncommon-subsequence-ii/ 

class Solution(object):
	def findLUSlength(self, strs):
		def subseqs(s, i):
			if i >= len(s):
				return {''}

			res = set()
			for sub in subseqs(s, i + 1):
				res.add(sub)
				res.add(s[i] + sub)

			return res

		repeats = set()
		allsubs = set()
		for s in strs:
			for sub in subseqs(s, 0):
				if sub in allsubs:
					repeats.add(sub)
				else:
					allsubs.add(sub)

		maxlen = -1
		for sub in allsubs:
			if sub not in repeats and len(sub) > maxlen:
				maxlen = len(sub)

		return maxlen

"""
After I solve a problem, I like to study other people's solutions. 

The above solution is a simple brute-force solution. Its time-complexity is O(N * 2**M), where N is the number of strings, and M is the length of a string. 

I found a solution that has a time-complexity of O(N**2 * M): https://leetcode.com/problems/longest-uncommon-subsequence-ii/discuss/99453/Python-Simple-Explanation
"""

class Solution(object):
	def findLUSlength(self, strs):
		def is_subseq(s1, s2):
			i = 0
			for c in s2:
				if i < len(s1) and s1[i] == c:
					i += 1
			return i == len(s1)

		strs = sorted(strs, key=len, reverse=True)
		for i, s1 in enumerate(strs):
			if not any(is_subseq(s1, s2) for j, s2 in enumerate(strs) if i != j):
				return len(s1)

		return -1
