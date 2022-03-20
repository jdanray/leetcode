# https://leetcode.com/problems/count-artifacts-that-can-be-extracted/ 

class Solution(object):
	def digArtifacts(self, n, artifacts, dig):
		xy2art = {}
		covered = {}
		for i, (r1, c1, r2, c2) in enumerate(artifacts):
			covered[i] = (r2 - r1 + 1) * (c2 - c1 + 1)
			for x in range(r1, r2 + 1):
				for y in range(c1, c2 + 1):
					xy2art[x, y] = i

		for (x, y) in dig:
			if (x, y) in xy2art:
				art = xy2art[x, y]
				covered[art] -= 1

		return len([art for art in covered if covered[art] == 0])


class Solution(object):
	def digArtifacts(self, n, artifacts, dig):
		dig = set((x, y) for (x, y) in dig)
		return sum(1 if all((x, y) in dig for x in range(r1, r2 + 1) for y in range(c1, c2 + 1)) else 0 for (r1, c1, r2, c2) in artifacts)
