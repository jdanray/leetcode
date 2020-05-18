# https://leetcode.com/problems/rearrange-words-in-a-sentence/ 

class Solution(object):
	def arrangeWords(self, text):
		words = text.split()
		words[0] = words[0].lower()

		count = collections.defaultdict(list)
		for w in words:
			l = len(w)
			count[l].append(w)

		rearr = []
		m = max(count.keys())
		for l in range(1, m + 1):
			rearr += count[l]

		rearr[0] = rearr[0][0].upper() + rearr[0][1:]
		rearr = ' '.join(rearr)

		return rearr
