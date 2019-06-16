# https://leetcode.com/problems/open-the-lock/

class Solution(object):
	def openLock(self, deadends, target):
		deadends = {tuple(int(d) for d in dead) for dead in deadends}
		target = tuple(int(t) for t in target)
		start = (0, 0, 0, 0)
		seen = set()
		queue = [[start, 0]]
		while queue:
			lock, n = queue.pop(0)

			if lock in deadends:
				continue

			if lock == target:
				return n

			for i in range(len(lock)):
				up = list(lock)
				up[i] += 1
				up[i] %= 10
				up = tuple(up)
				if up not in seen:
					seen.add(up)
					queue.append([up, n + 1])

				down = list(lock)
				down[i] -= 1
				down[i] %= 10
				down = tuple(down)
				if down not in seen:
					seen.add(down)
					queue.append([down, n + 1])

		return -1
