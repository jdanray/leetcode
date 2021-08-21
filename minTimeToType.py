# https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/

class Solution(object):
	def minTimeToType(self, word):
		index = {c: i for i, c in enumerate(string.ascii_lowercase)}
		N = len(index)

		pointer = 0
		res = 0
		for c in word:
			i = index[c]
			res += min((i - pointer) % N, (pointer - i) % N)
			res += 1
			pointer = i

		return res
