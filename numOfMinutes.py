# https://leetcode.com/problems/time-needed-to-inform-all-employees/ 

class Solution(object):
	def numOfMinutes(self, n, headID, manager, informTime):
		subs = collections.defaultdict(list)
		for i, e in enumerate(manager):
			subs[e].append(i)

		stack = [[headID, 0]]
		res = 0
		while stack:
			e, t = stack.pop()

			res = max(res, t)

			for s in subs[e]:
				stack.append([s, t + informTime[e]])

		return res
