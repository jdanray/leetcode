# https://leetcode.com/problems/pyramid-transition-matrix/ 

class Solution(object):
	def pyramidTransition(self, bottom, allowed):
		triangle = collections.defaultdict(set)
		for a in allowed:
			triangle[a[0] + a[1]].add(a[2])

		memo = {}
		def check(bottom):
			if len(bottom) == 1:
				return True

			if bottom in memo:
				return memo[bottom]

			tops = ['']
			for i in range(len(bottom) - 1):
				p = bottom[i] + bottom[i + 1]

				if p not in triangle:
					return False

				newTops = []
				for r in triangle[p]:
					for t in tops:
						newTops.append(t + r)
				tops = newTops

			memo[bottom] = any(check(t) for t in tops)
			return memo[bottom]

		return check(bottom)

class Solution:
	def allperms(self, blocks, p='', i=0):
		if i >= len(blocks):
			return [p]

		res = []
		for b in blocks[i]:
			res += self.allperms(blocks, p + b, i + 1)
		return res

	def pyramidTransition(self, bottom, allowed):
		ruleset = collections.defaultdict(list)
		for rule in allowed:
			ruleset[rule[:2]].append(rule[2])
	
		memo = {}	
		def helper(bottom):
			if len(bottom) == 1:
				return True

			if bottom in memo:
				return memo[bottom]

			cands = []
			for i in range(len(bottom) - 1):
				left = bottom[i]
				right = bottom[i + 1]
				rule = left + right

				if rule not in ruleset:
					return False

				cands.append(ruleset[rule])

			memo[bottom] = any(helper(p) for p in self.allperms(cands))
			return memo[bottom]

		return helper(bottom)
