# https://leetcode.com/problems/online-election/

class TopVotedCandidate(object):
	def __init__(self, persons, times):
		self.times = times
		self.leader = []
		lead = -1
		votes = collections.defaultdict(int)
		for p, t in zip(persons, times):
			votes[p] += 1
			if votes[p] >= votes[lead]:
				lead = p                
			self.leader.append(lead)

	def q(self, t):
		return self.leader[bisect.bisect(self.times, t) - 1]
