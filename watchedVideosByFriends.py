# https://leetcode.com/problems/get-watched-videos-by-your-friends/

class Solution(object):
	def watchedVideosByFriends(self, watchedVideos, friends, id, level):
		freq = collections.defaultdict(int)
		seen = {id}
		queue = [[id, level]]
		while queue:
			id, lvl = queue.pop(0)

			if lvl == 0:
				for video in watchedVideos[id]:
					freq[video] += 1
				continue

			for u in friends[id]:
				if u not in seen:
					queue.append([u, lvl - 1])
					seen.add(u)

		return sorted(sorted(freq), key=lambda v: freq[v])
