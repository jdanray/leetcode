# https://leetcode.com/problem/relative-ranks/

class Solution:
	def findRelativeRanks(self, nums):
		N = len(nums)
		medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
		iranks = [i for i in sorted(range(N), key=lambda i: nums[i], reverse=True)]
		ranks = [""] * N

		for i, ir in enumerate(iranks):
			if i < len(medals):
				ranks[ir] = medals[i]
			else:
				ranks[ir] = str(i + 1)
		return ranks

# I came up with a (hopefully) more elegant solution:
class Solution(object):
	def findRelativeRanks(self, score):
		place = ["Gold Medal", "Silver Medal", "Bronze Medal"]
		rank = {s: i for i, s in enumerate(sorted(score, reverse=True))}

		res = []
		for s in score:
			if rank[s] < len(place):
				res.append(place[rank[s]])
			else:
				res.append(str(rank[s] + 1))

		return res

# Streamline the above solution a bit:
class Solution(object):
	def findRelativeRanks(self, score):
		place = ["Gold Medal", "Silver Medal", "Bronze Medal"]
		rank = {s: i for i, s in enumerate(sorted(score, reverse=True))}
		return [place[rank[s]] if rank[s] < len(place) else str(rank[s] + 1) for s in score]
