# https://leetcode.com/problems/defanging-an-ip-address/

class Solution(object):
	def defangIPaddr(self, address):
		return "".join("[.]" if a == "." else a for a in address)

class Solution(object):
	def defangIPaddr(self, address):
		res = ""
		for a in address:
			if a == ".":
				res += "[.]"
			else:
				res += a
		return res
