# https://leetcode.com/problems/ransom-note/description/

class Solution(object):
	def canConstruct(self, ransomNote, magazine):
		countR = collections.Counter(ransomNote)
		countM = collections.Counter(magazine)
		return all(countR[l] <= countM[l] for l in countR)

class Solution:
	def canConstruct(self, ransomNote, magazine):
		notect = dict()
		magct = dict()
		for m in magazine:
			if m not in magct:
				magct[m] = 0
			magct[m] += 1
		for n in ransomNote:
			if n not in magct:
				return False
			if n not in notect:
				notect[n] = 0
			notect[n] += 1
		for n in notect:
			if notect[n] > magct[n]:
				return False
		return True
