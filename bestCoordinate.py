# https://leetcode.com/problems/coordinate-with-maximum-network-quality/ 

class Solution(object):
	def bestCoordinate(self, towers, radius):
		def dist(x1, y1, x2, y2): 
			return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

		maxnet = 0
		res = [-1, -1]
		for (x1, y1, _) in towers:
			network = 0
			for (x2, y2, q) in towers:
				d = dist(x1, y1, x2, y2)
				if d <= radius:
					signal = math.floor(q / (1 + d))
					network += signal 

			if network > maxnet or (network == maxnet and (x1, y1) < (res[0], res[1])):
				maxnet = network
				res = [x1, y1]

		return res
