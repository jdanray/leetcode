#  https://leetcode.com/problems/html-entity-parser/ 

class Solution(object):
	entity = {}
	entity["&quot;"] = "\""
	entity["&apos;"] = "'"
	entity["&amp;"] = "&"
	entity["&gt;"] = ">"
	entity["&lt;"] = "<"
	entity["&frasl;"] = "/"

	def entityParser(self, text):
		N = len(text)
		i = 0
		res = ""
		while i < N:
			if text[i] == "&":
				add = ""
				while i < N and text[i] != ";":
					add += text[i]
					i += 1

				if i < N and text[i] == ";":
					add += text[i]

				if add in self.entity:
					add = self.entity[add]
				res += add
			else:
				res += text[i]
			i += 1
		return res
