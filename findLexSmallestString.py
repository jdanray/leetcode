# https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/ 

class Solution(object):
	def findLexSmallestString(self, s, a, b):
		seen = {s}
		res = s
		stack = [s]
		while stack:
			chars = stack.pop()

			res = min(res, chars)

			# apply operation 1

			chars1 = ''
			for i, c in enumerate(chars):
				if i % 2 == 0:
					chars1 += c
				else:
					d = (int(c) + a) % 10
					chars1 += str(d)

			if chars1 not in seen:
				stack.append(chars1)
				seen.add(chars1)

			# apply operation 2

			chars2 = chars[-b:] + chars[:-b]

			if chars2 not in seen:
				stack.append(chars2)
				seen.add(chars2)

		return res
