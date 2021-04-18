# https://leetcode.com/problems/single-threaded-cpu/ 
 
class Solution(object):
	def getOrder(self, tasks):
		N = len(tasks)
		tasks = sorted([e, p, i] for i, (e, p) in enumerate(tasks))
		avail = []
		t = 1
		i = 0
		res = []
		while i < N or avail:
			while i < N and t >= tasks[i][0]:
				heapq.heappush(avail, (tasks[i][1], tasks[i][2]))
				i += 1

			if avail:
				p, idx = heapq.heappop(avail)
				res.append(idx)
				t += p
			elif i < N and t < tasks[i][0]:
				t = tasks[i][0]
            
		return res
