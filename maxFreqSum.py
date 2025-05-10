# https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/

class Solution(object):
	def maxFreqSum(self, s):
		vowels = 'aeiou'

		mv = 0
		mc = 0
		cv = collections.Counter()
		cc = collections.Counter()
		for c in s:
			if c in vowels:
				cv[c] += 1
			else:
				cc[c] += 1

			mv = max(mv, cv[c])
			mc = max(mc, cc[c])

		return mv + mc

class Solution(object):
	def maxFreqSum(self, s):
		vowels = set('aeiou')
		cons = set(string.ascii_lowercase) - vowels

		cv = collections.Counter(c for c in s if c in vowels).values()
		cc = collections.Counter(c for c in s if c in cons).values()

		mv = max(cv) if cv else 0
		mc = max(cc) if cc else 0

		return mc + mv