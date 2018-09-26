# https://leetcode.com/problems/most-frequent-subtree-sum/description/

class Solution(object):
	def findFrequentTreeSum(self, root):
		if not root:
			return []

		freq = {}
		def subtreesum(root):
			if not root:
				return 0

			l = subtreesum(root.left)
			r = subtreesum(root.right)
			s = root.val + l + r

			if s not in freq:
				freq[s] = 1
			else:
				freq[s] += 1

			return s

		subtreesum(root)
		m = max(freq.values())
		return [v for v in freq if freq[v] == m]
