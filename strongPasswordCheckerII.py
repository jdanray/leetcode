# https://leetcode.com/problems/strong-password-checker-ii/ 

class Solution(object):
	def strongPasswordCheckerII(self, pwd):
		special = "!@#$%^&*()-+"
		L = 8

		if len(pwd) < L:
			return False

		if not any(l in pwd for l in string.ascii_lowercase):
			return False

		if not any(u in pwd for u in string.ascii_uppercase):
			return False

		if not any(d in pwd for d in string.digits):
			return False

		if not any(s in pwd for s in special):
			return False

		if any(pwd[i] == pwd[i - 1] for i in range(1, len(pwd))):
			return False

		return True

class Solution(object):
	def strongPasswordCheckerII(self, pwd):
		special = "!@#$%^&*()-+"
		L = 8

		if len(pwd) < L:
			return False

		lower = False
		upper = False
		digit = False
		spec = False
		for i, c in enumerate(pwd):
			if i > 0 and pwd[i] == pwd[i - 1]:
				return False

			if c in string.ascii_lowercase:
				lower = True

			if c in string.ascii_uppercase:
				upper = True

			if c in string.digits:
				digit = True

			if c in special:
				spec = True

		return lower and upper and digit and spec
