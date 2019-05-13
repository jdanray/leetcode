# https://leetcode.com/problems/satisfiability-of-equality-equations/ 

class Solution(object):
	def reach(self, start, dest, graph):
		seen = {start}
		stack = [start]
		while stack:
			u = stack.pop() 

			if u == dest:
				return True

			for v in graph[u]:
				if v not in seen:
					seen.add(v)
					stack.append(v)	

		return False 

	def equationsPossible(self, equations):
		equals = collections.defaultdict(set)
		unequals = set()
		for eq in equations:
			x = eq[0]
			y = eq[3]

			if eq[1] == "!":
				unequals.add((x, y))
			else:
				equals[x].add(y)
				equals[y].add(x)

		return not any(self.reach(x, y, equals) for (x, y) in unequals)
