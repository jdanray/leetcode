# https://leetcode.com/problems/remove-methods-from-project/ 

class Solution(object):
	def remainingMethods(self, n, k, invocations):
		graph = collections.defaultdict(set)
		for (u, v) in invocations:
			graph[u].add(v)

		seen = {k}
		stack = [k]
		while stack:
			u = stack.pop()            
			for v in graph[u]:
				if v not in seen:
					seen.add(v)
					stack.append(v)

		for (u, v) in invocations:
			if v in seen and u not in seen:
				return list(range(n))

		return [u for u in range(n) if u not in seen]
