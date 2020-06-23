# https://leetcode.com/problems/compare-version-numbers/

class Solution(object):
	def compareVersion(self, version1, version2):
		def trimZeros(version):
			i = 0
			while i < len(version) and version[i] == '0':
				i += 1

			version = version[i:]
			return version

		def compare(v1, v2):
			v1 = trimZeros(v1)
			v2 = trimZeros(v2)

			if len(v1) > len(v2):
				return 1
			elif len(v1) < len(v2):
				return -1

			for i in range(len(v1)):
				if v1[i] > v2[i]:
					return 1
				elif v1[i] < v2[i]:
					return -1

			return 0

		def splitup(v1, v2):
			v1 = v1.split('.')
			v2 = v2.split('.')

			if len(v1) > len(v2):
				v2 += [''] * (len(v1) - len(v2))
			elif len(v1) < len(v2):
				v1 += [''] * (len(v2) - len(v1))

			return v1, v2

		v1, v2 = splitup(version1, version2)
		for i in range(len(v1)):
			c = compare(v1[i], v2[i])
			if c != 0:
				return c
            
		return 0
