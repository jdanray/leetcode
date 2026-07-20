# https://leetcode.com/problems/rearrange-string-to-avoid-character-pair/

class Solution(object):
	def rearrangeString(self, s, x, y):
		count = collections.Counter(s)
		return (y * count[y]) + ''.join(c * count[c] for c in count if c != x and c != y) + (x * count[x])

class Solution(object):
	def rearrangeString(self, s, x, y):
		count = collections.Counter(s)

		res = y * count[y]

		for c in count:
			if c != x and c != y:
				res += c * count[c]

		res += x * count[x]

		return res