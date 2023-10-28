// https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/ 

class Solution {
	private int memo[][];

	private int dp(int i, int t, List<Integer> nums) {
		if (t == 0) { 
			return 0;
		}

		if (t < 0 || i >= nums.size()) {
			return Integer.MIN_VALUE;
		}

		if (memo[i][t] != -1) {
			return memo[i][t];
		}

		int incl = 1 + dp(i + 1, t - nums.get(i), nums);
		int excl = dp(i + 1, t, nums);

		memo[i][t] = Math.max(incl, excl);
		return memo[i][t];
	}

	public int lengthOfLongestSubsequence(List<Integer> nums, int target) {
		memo = new int[nums.size() + 1][target + 1];
		for (int[] row : memo) {
			Arrays.fill(row, -1);
		}

		int res = dp(0, target, nums);
		return res > 0 ? res : -1;
	} 
}
