# https://leetcode.com/problems/unique-morse-code-words/description/

class Solution:
	morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'}
	def uniqueMorseRepresentations(self, words):
		reps = set()
		for w in words:
			t = ''
			for c in w:
				t += self.morse[c]
			reps.add(t)
		return len(reps)
