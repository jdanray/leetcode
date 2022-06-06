# https://leetcode.com/problems/sender-with-largest-word-count/

class Solution(object):
	def largestWordCount(self, messages, senders):
		count = collections.Counter()
		for i, m in enumerate(messages):
			s = senders[i]
			words = m.split()
			count[s] += len(words)

		maxim = max(count.values())
		cands = [c for c in count if count[c] == maxim]
		cands = sorted(cands, reverse=True)

		return cands[0]
