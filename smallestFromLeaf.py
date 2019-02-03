# https://leetcode.com/problems/smallest-string-starting-from-leaf/

class Solution(object):
	def smallestFromLeaf(self, root):
		minseq = ()
		stack = [[root, []]]
		while stack:
			node, seq = stack.pop()

			if not node:
				continue

			seq = [node.val] + seq

			if not node.left and not node.right:
				seq = tuple(seq)
				if not minseq or seq < minseq:
					minseq = seq
			
			stack.append([node.left, seq])
			stack.append([node.right, seq])

		alphabet = 'abcdefghijklmnopqrstuvwxyz'
		return ''.join(alphabet[n] for n in minseq)
