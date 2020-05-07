# https://leetcode.com/problems/encode-and-decode-tinyurl/

class Codec:
	prefix = "http://tinyurl.com/"
	suffix = ""
	code = {}

	def encode(self, longUrl):
		self.suffix += 'a'
		url = self.prefix + self.suffix
		self.code[url] = longUrl
		return url 

	def decode(self, shortUrl):
		return self.code[shortUrl]
