# https://leetcode.com/problems/number-of-lines-to-write-string/description/

class Solution:
	def numberOfLines(self, widths, S):
		if not S:
			return [0, 0]
		alpha = 'abcdefghijklmnopqrstuvwxyz'
		c_to_i = {c: i for i in range(alpha)}
		nlines = 1
		used = 0
		maxwidth = 100
		for c in S:
			i = c_to_i[c]
			w = widths[i]
			if used + w > maxwidth:
				nlines += 1
				used = w
			else:
				used += w
		return [nlines, used]
