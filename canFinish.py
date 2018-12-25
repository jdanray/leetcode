# https://leetcode.com/problems/course-schedule/description/

class Solution(object):
	def canFinish(self, numCourses, prereqs):
		components = []
		idx = 0	
		index = dict()
		lowlink = dict()
		onstack = dict()
		stack = []

		def tarjan(v, idx, index, lowlink, onstack, stack):
			index[v] = idx
			lowlink[v] = idx
			idx += 1
			stack.append(v)
			onstack[v] = True

			if v in graph:
				for w in graph[v]:
					if not w in index:
						tarjan(w, idx, index, lowlink, onstack, stack)
						lowlink[v] = min(lowlink[v], lowlink[w])
					elif w in onstack and onstack[w]:
						lowlink[v] = min(lowlink[v], index[w])

			if lowlink[v] == index[v]:
				comp = []
				w = stack.pop()
				onstack[w] = False
				comp.append(w)
				while w != v:
					w = stack.pop()
					onstack[w] = False
					comp.append(w)
				components.append(comp)

		graph = dict()
		for u, v in prereqs:
			if u == v:
				return False
			if u not in graph:
				graph[u] = set()
			graph[u].add(v)
	
		for u, v in prereqs:
			if u not in index:
				tarjan(u, idx, index, lowlink, onstack, stack)
			if v not in index:
				tarjan(v, idx, index, lowlink, onstack, stack)

		return all(len(c) == 1 for c in components)
