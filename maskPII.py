# https://leetcode.com/problems/masking-personal-information/ 

class Solution(object):
	def maskPII(self, s):
		def maskEmail(s):
			s = s.lower()
			name, domain = s.split("@")
			return name[0] + "*****" + name[-1] + "@" + domain

		def maskPhone(s):
			sep = {"+", "-", "(", ")", " "}
			num = "".join(c for c in s if c not in sep)

			res = "***-***-" + str(num[-4:])
			if len(num) == 10:
				return res
			else:
				return "+" + ("*" * (len(num) - 11)) + "*-" + res

		if "@" in s:
			return maskEmail(s)
		else:
			return maskPhone(s)
