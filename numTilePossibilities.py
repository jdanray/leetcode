# https://leetcode.com/problems/letter-tile-possibilities/

class Solution(object):
	def numTilePossibilities(self, tiles):
		seqs = set()
		def build(used, s):
			seqs.add(s)
			for i, t in enumerate(tiles):
				if (used >> i) & 1 == 0:
					build(used ^ (1 << i), s + t)

		build(0, '')
		return len(seqs) - 1
