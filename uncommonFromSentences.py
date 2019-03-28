# https://leetcode.com/problems/uncommon-from-two-sentences/

from collections import Counter

class Solution:
	def uncommonFromSentences(self, A, B):
		def uncommon(split1, split2):
			count = Counter(split1)
			return [c for c in count if count[c] == 1 and c not in set(split2)]

		split1 = A.split()
		split2 = B.split()
		return uncommon(split1, split2) + uncommon(split2, split1)
