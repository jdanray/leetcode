# https://leetcode.com/problems/valid-word/ 

class Solution(object):
	def isValid(self, word):
		vowels = set('AEIOUaeiou')
		consonants = set(string.ascii_lowercase + string.ascii_uppercase) - set(vowels)

		return len(word) >= 3 and word.isalnum() and any(v in word for v in vowels) and any(c in word for c in consonants)
