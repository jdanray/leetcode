# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

class Solution(object):
	def minDeletions(self, s):
		freq = collections.Counter(s)
		count = collections.defaultdict(int)
		m = 0
		for f in freq.values():
			count[f] += 1
			m = max(m, f)

		res = 0
		zeros = []
		for i in range(m + 1):
			if count[i] == 0:
				heapq.heappush(zeros, -i)

			while count[i] > 1:
				if zeros:
					z = heapq.heappop(zeros)
					z = abs(z)
				else:
					z = 0

				count[z] = 1
				count[i] -= 1

				res += (i - z)

		return res
