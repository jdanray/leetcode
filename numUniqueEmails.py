# https://leetcode.com/problems/unique-email-addresses/

class Solution(object):
	def numUniqueEmails(self, emails):
		unique = set()
		for mail in emails:
			i = 0
			local = ''
			plus = False
			while mail[i] != "@":
				if mail[i] == '.':
					i += 1
				elif mail[i] == '+' or plus:
					plus = True
					i += 1
				else:
					local += mail[i]
					i += 1
			unique.add(local + mail[i:])
		return len(unique)
