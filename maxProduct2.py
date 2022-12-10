# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/

class Solution(object):
	def maxProduct(self, root):
		MOD = 10**9 + 7

		sums = collections.defaultdict(int)
		def calcSums(node):
			if not node:
				return 0

			sums[node] = node.val + calcSums(node.left) + calcSums(node.right)
			return sums[node]

		prods = {}
		def calcProds(node):
			if not node:
				return False

			l = (sums[node.left] * (sums[root] - sums[node.left]))
			r = (sums[node.right] * (sums[root] - sums[node.right]))
			prods[node] = max(l, r)

			calcProds(node.left)
			calcProds(node.right)

		calcSums(root)
		calcProds(root)
		return max(prods.values()) % MOD
