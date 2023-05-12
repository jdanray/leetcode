# https://leetcode.com/problems/shifting-letters-ii/

class Solution(object):
	def shiftingLetters(self, s, shifts):
		alphabet = string.ascii_lowercase
		char2idx = {c: i for i, c in enumerate(alphabet)}

		change = [0 for _ in range(len(s) + 1)]
		for (b, e, d) in shifts:
			if d == 1:
				change[b] += 1
				change[e + 1] -= 1
			else:
				change[b] -= 1
				change[e + 1] += 1

		for i in range(1, len(change)):
			change[i] += change[i - 1]

		res = ''
		for i, c in enumerate(s):
			j = (char2idx[c] + change[i]) % len(alphabet)
			res += alphabet[j]

		return res
