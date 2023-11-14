# https://leetcode.com/problems/high-access-employees/ 

class Solution(object):
	def findHighAccessEmployees(self, access_times):
		acc = collections.defaultdict(list)
		for (n, a) in access_times:
			t = int(a[:2]) * 60 + int(a[2:])
			acc[n].append(t)

		res = []
		for n in acc:
			acc[n] = sorted(acc[n])
			for i in range(len(acc[n]) - 2):
				if acc[n][i] + 60 > acc[n][i + 2]:
					res.append(n)
					break

		return res
