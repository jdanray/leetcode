# https://leetcode.com/problems/find-the-sequence-of-strings-appeared-on-the-screen/

class Solution(object):
	def stringSequence(self, target):
		res = []
		for c in target:
			seq = []
			for a in string.ascii_lowercase:
				seq.append(a)
				if a == c:
					break

			head = res[-1] if res else ''
			for tail in seq:
				res.append(head + tail)

		return res