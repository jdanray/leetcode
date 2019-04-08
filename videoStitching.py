# https://leetcode.com/problems/video-stitching/

class Solution(object):
	def videoStitching(self, clips, T):
		start = 0
		n = 0
		i = 0
		clips = sorted(clips, key=lambda c: c[0])
		while i < len(clips) and start < T:
			best = -1
			while i < len(clips) and clips[i][0] <= start:
				if clips[i][1] > best:
					best = clips[i][1]
				i += 1

			if best == -1:
				return -1

			start = best
			n += 1

		if start < T:
			return -1

		return n
