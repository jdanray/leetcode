# https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/

class Solution(object):
	def alertNames(self, keyName, keyTime):
		N = len(keyName)
		times = collections.defaultdict(list)
		for i in range(N):
			h, m = keyTime[i].split(':')
			times[keyName[i]].append(60 * int(h) + int(m))

		res = []
		for name in sorted(times):
			st = sorted(times[name])
			for i in range(len(st) - 2):
				if st[i + 2] - st[i] <= 60:
					res.append(name)
					break

		return res
