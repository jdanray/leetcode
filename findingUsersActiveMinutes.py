# https://leetcode.com/problems/finding-the-users-active-minutes/ 

class Solution(object):
	def findingUsersActiveMinutes(self, logs, k):
		uam = collections.defaultdict(set)
		for (uid, min) in logs:
			uam[uid].add(min)

		nusers = collections.Counter()
		for uid in uam:
			l = len(uam[uid])
			nusers[l] += 1

		return [nusers[l] for l in range(1, k + 1)]
