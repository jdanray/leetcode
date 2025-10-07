# https://leetcode.com/problems/avoid-flood-in-the-city/

class Solution(object):
	def avoidFlood(self, rains):
		N = len(rains)

		full = collections.defaultdict(bool)
		dry = []

		idx = collections.defaultdict(list)		
		for i in range(N - 1, -1, -1):
			if rains[i] != 0:
				idx[rains[i]].append(i)

		res = [-1 for _ in range(N)]
		for i, r in enumerate(rains):
			if r == 0:
				if dry:
					_, l = heapq.heappop(dry)
				else:
					l = 1
				full[l] = False
				res[i] = l
			elif full[r]:
				return []
			else:
				idx[r].pop()
				if idx[r]:
					heapq.heappush(dry, (idx[r][-1] - i, r))
				full[r] = True

		return res