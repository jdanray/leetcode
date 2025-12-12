# https://leetcode.com/problems/count-mentions-per-user/

class Solution(object):
	def countMentions(self, numUsers, events):
		events = sorted([[int(t), 0 if e == 'OFFLINE' else 1, m] for (e, t, m) in events])
		offline = collections.deque([])
		res = [0 for _ in range(numUsers)]
		for (ts, et, mentions) in events:
			if et == 0:
				offline.append([ts + 60, int(mentions)])
				continue

			for m in mentions.split():
				if m[0] == 'i':
					i = int(m[2:])
					res[i] += 1
					continue

				for i in range(numUsers):
					res[i] += 1

				if m == 'ALL':
					continue

				while offline and ts >= offline[0][0]:
					offline.popleft()

				for (_, i) in offline:
					res[i] -= 1

		return res