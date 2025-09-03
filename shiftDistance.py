# https://leetcode.com/problems/shift-distance-between-two-strings/

class Solution(object):
	def shiftDistance(self, s, t, nextCost, prevCost):
		charIdx = {c: i for i, c in enumerate(string.ascii_lowercase)}

		res = 0
		for i, c in enumerate(s):
			k = charIdx[t[i]]

			# prev
			j = charIdx[c]
			p = 0
			while j != k:
				p += prevCost[j]
				j -= 1
				j %= len(prevCost)

			# next
			j = charIdx[c]
			n = 0
			while j != k:
				n += nextCost[j]
				j += 1
				j %= len(nextCost)

			res += min(p, n)

		return res