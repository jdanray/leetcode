// https://leetcode.com/problems/length-of-last-word/

class Solution {
	public int lengthOfLastWord(String s) {
		int i, n;
		for (i = s.length() - 1; i >= 0 && s.charAt(i) == ' '; i--);
		for (i = i, n = 0; i >= 0 && s.charAt(i) != ' '; i--, n++);
		return n;
	}
}
