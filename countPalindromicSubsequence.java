// https://leetcode.com/problems/unique-length-3-palindromic-subsequences/

class Solution {
	public int countPalindromicSubsequence(String s) {
		int res = 0;
		for (char p = 'a'; p <= 'z'; p++) {
			int start = s.indexOf(p);
			if (start == -1)
				continue;

			Set<String> seen = new HashSet<>();
			Set<String> used = new HashSet<>();
			for (int i = start + 1; i < s.length(); i++) {
				if (s.charAt(i) == p) {
					for (String c : seen) {
						if (!used.contains(c)) {
							res++;
							used.add(c);
						}
					}
					seen.clear();
				}
				seen.add(String.valueOf(s.charAt(i)));
			}
		}

		return res;
	}
}