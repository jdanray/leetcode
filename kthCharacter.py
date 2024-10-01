# https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/ 

class Solution(object):
	def kthCharacter(self, k):
		def helper(k):
			if k == 1:
				return 0

			n = 2 ** math.ceil(math.log(k, 2))
			return helper(k - (n // 2)) + 1

		i = helper(k) % len(string.ascii_lowercase)
		return string.ascii_lowercase[i]
