# https://leetcode.com/problems/reconstruct-original-digits-from-english/

from collections import Counter

class Solution:
	def originalDigits(self, s):
		decrypt = [('z', 'zero', 0), ('w', 'two', 2), ('x', 'six', 6), ('g', 'eight', 8), ('u', 'four', 4), ('t', 'three', 3), ('o', 'one', 1), ('s', 'seven', 7), ('f', 'five', 5), ('i', 'nine', 9)]
		count = Counter(s)
		digits = []

		for (id, name, dig) in decrypt:
			n = count[id]
			if n > 0:
				digits += [dig] * n
				for c in name:
					count[c] -= n

		return "".join(map(str, sorted(digits)))
