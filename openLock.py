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

class Solution(object):
	def openLock(self, deadends, target):
		start = "0000"
		change = {str(n): [str((n - 1) % 10), str((n + 1) % 10)] for n in range(10)}
		deadends = set(deadends)
		seen = set()
		queue = [[start, 0]]
		while queue:
			lock, nturns = queue.pop(0)

			if lock in deadends:
				continue

			if lock == target:
				return nturns

			for i, l in enumerate(lock):
				for c in change[l]:
					newlock = lock[:i] + c + lock[i + 1:]
					if newlock not in seen:
						seen.add(newlock)
						queue.append([newlock, nturns + 1])

		return -1

class Solution(object):
	def openLock(self, deadends, target):
		NSLOTS = 10
		start = '0000'
		deadends = set(deadends)

		seen = {start}
		queue = collections.deque([[start, 0]])
		while queue:
			u, nsteps = queue.popleft()

			if u in deadends:
				continue

			if u == target:
				return nsteps

			for i in range(len(u)):
				for d in [1, -1]:
					v = u[:i] + str((d + int(u[i])) % NSLOTS) + u[i + 1:]
					if v not in seen:
						queue.append([v, nsteps + 1])
						seen.add(v)

		return -1
