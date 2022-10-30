# https://leetcode.com/problems/most-popular-video-creator/ 

class Solution(object):
	def mostPopularCreator(self, creators, ids, views):
		popularity = collections.Counter()
		mv = {}
		for i, c in enumerate(creators):
			popularity[c] += views[i]

			if c not in mv or views[i] > mv[c][0] or (views[i] == mv[c][0] and ids[i] < mv[c][1]):
				mv[c] = (views[i], ids[i])

		res = []
		for c in popularity:
			p = popularity[c]

			if not res or p > popularity[res[0][0]]:
				res = [[c, mv[c][1]]]
			elif res and p == popularity[res[0][0]]:
				res.append([c, mv[c][1]])

		return res 
