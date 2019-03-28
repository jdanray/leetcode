# https://leetcode.com/problems/most-common-word/

from collections import Counter

class Solution(object):
	def mostCommonWord(self, paragraph, banned):
		para = paragraph.replace(",", " ")
		punc = set("!?';.")
		para = ''.join(c for c in para if c not in punc)
		para = para.split()

		banned = set(banned)
		count = Counter(w.lower() for w in para)
		return max([w for w in count if w not in banned], key=lambda w: count[w])
