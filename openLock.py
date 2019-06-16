# https://leetcode.com/problems/open-the-lock/

class Solution(object):
	def openLock(self, deadends, target):
		deadends = {tuple(int(d) for d in dead) for dead in deadends}
		start = [0, 0, 0, 0]
		target = [int(t) for t in target]
		seen = set()
		queue = [[start, 0]]
		while queue:
			lock, n = queue.pop(0)

			if tuple(lock) in deadends:
				continue

			if lock == target:
				return n

			for i in range(len(lock)):
				up = list(lock)
				up[i] += 1
				up[i] %= 10
				tup = tuple(up)
				if tup not in seen:
					seen.add(tup)
					queue.append([up, n + 1])

				down = list(lock)
				down[i] -= 1
				down[i] %= 10
				tdown = tuple(down)
				if tdown not in seen:
					seen.add(tdown)
					queue.append([down, n + 1])

		return -1
