# https://leetcode.com/problems/find-good-days-to-rob-the-bank/ 

class Solution(object):
	def goodDaysToRobBank(self, security, time):
		N = len(security)

		noninc = [0 for _ in range(N)]
		nondec = [0 for _ in range(N)]
        
		for i in range(1, N):
			if security[i] <= security[i - 1]: 
				noninc[i] = noninc[i - 1] + 1

			if security[N - i - 1] <= security[N - i]:
				nondec[N - i - 1] = nondec[N - i] + 1

		return [i for i in range(N) if noninc[i] >= time and nondec[i] >= time]
