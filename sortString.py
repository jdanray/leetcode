# https://leetcode.com/problems/increasing-decreasing-string/

class Solution(object):
	def sortString(self, s):
		res = ""
		count = collections.Counter(s)
		keys = sorted(count.keys())
		revkeys = keys[::-1]
		backward = False
		appending = True
		while appending:
			if backward:
				choice = revkeys
			else:
				choice = keys

			appending = False
			for k in choice:
				if count[k] > 0:
					res += k
					count[k] -= 1
					appending = True

			backward = not backward

		return res
