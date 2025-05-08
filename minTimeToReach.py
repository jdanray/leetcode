# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/

class Solution(object):
	def minTimeToReach(self, moveTime):
		deltas = [[1, 0], [-1, 0], [0, 1], [0, -1]]
		M = len(moveTime)
		N = len(moveTime[0])

		dist = dict()
		for i in range(M):
			for j in range(N):
				dist[i, j] = float('inf')
		dist[0, 0] = 0

		pq = [[0, 0, 0]]
		heapq.heapify(pq)
        
		while pq:
			t, i, j = heapq.heappop(pq)

			for (di, dj) in deltas:
				ni = i + di
				nj = j + dj

				if ni < 0 or ni >= M or nj < 0 or nj >= N:
					continue

				w = 1 + max(t, moveTime[ni][nj])
				if dist[ni, nj] > w:
					dist[ni, nj] = w
					heapq.heappush(pq, (dist[ni, nj], ni, nj))

		return dist[M - 1, N - 1]