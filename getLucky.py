# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution(object):
	def getLucky(self, s, k):
		alphabet = string.ascii_lowercase
		atoi = {a: i + 1 for i, a in enumerate(alphabet)}

		def transform(num):
			res = 0
			while num > 0:
				digit = num % 10
				res += digit
				num //= 10
			return res

		num = 0
		for a in s:
			i = atoi[a]
			num += transform(i)

		for _ in range(k - 1):
			num = transform(num)

		return num
