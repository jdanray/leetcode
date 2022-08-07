# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/ 

class Solution(object):
	def closestMeetingNode(self, edges, node1, node2):
		def getDist(u):
			dist = collections.defaultdict(int)
			d = 0
			while u != -1 and u not in dist:
				dist[u] = d
				d += 1
				u = edges[u]
			return dist

		dist1 = getDist(node1)
		dist2 = getDist(node2)

		res = -1
		minim = float('inf')
		for u in range(len(edges)):
			if u not in dist1 or u not in dist2:
				continue

			m = max(dist1[u], dist2[u])
			if m < minim:
				minim = m
				res = u
                
		return res

class Solution(object):
	def closestMeetingNode(self, edges, node1, node2):
		dist = collections.defaultdict(int)
		d = 0
		u = node1
		while u != -1 and u not in dist:
			dist[u] = d
			d += 1
			u = edges[u]

		seen = set()
		d = 0
		u = node2
		res = -1
		minim = float('inf')
		while u != -1 and u not in seen:
			if u in dist:
				m = max(dist[u], d)
				if m < minim or (m == minim and u < res):
					minim = m
					res = u

			seen.add(u)
			d += 1
			u = edges[u]               

		return res
