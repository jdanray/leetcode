# https://leetcode.com/problems/maximum-score-words-formed-by-letters/

class Solution(object):
	def maxScoreWords(self, words, letters, score):
		alphabet = "abcdefghijklmnopqrstuvwxyz"
		lscore = {a: score[i] for i, a in enumerate(alphabet)}
		wcount = [collections.Counter(w) for w in words]
		lcount = collections.Counter(letters)

		def helper(i, count):
			if i >= len(words):
				return 0

			skip = helper(i + 1, count)
			if all(l in count and l in wcount[i] and wcount[i][l] <= count[l] for l in words[i]):
				newcount = dict(count)
				for l in words[i]:
					newcount[l] -= 1
				return max(helper(i + 1, newcount) + sum(lscore[l] for l in words[i]), skip)
			else:
				return skip

		return helper(0,  lcount)
