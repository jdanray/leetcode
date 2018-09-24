# https://leetcode.com/problems/queue-reconstruction-by-height/description/

from functools import cmp_to_key

class Solution:
	def reconstructQueue(self, people):
		def cmp(p1, p2):
			h1, k1 = p1
			h2, k2 = p2

			if h1 > h2:
				return -1
			elif h1 < h2:
				return 1
			elif k1 < k2:
				return -1
			else:
				return 1

		queue = []
		for p in sorted(people, key=cmp_to_key(cmp)):
			queue.insert(p[1], p)

		return queue
