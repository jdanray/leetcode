// https://leetcode.com/problems/unique-paths-ii/submissions/ 

public class Solution {
	public int uniquePathsWithObstacles(int[][] grid) {
		int M = grid.length;
		int N = grid[0].length;

		int[][] dp = new int[M][N];
		dp[0][0] = 1 - grid[0][0];

		for (int i = 0; i < M; i++) {
			for (int j = 0; j < N; j++) {
				if (grid[i][j] == 1)
					continue;

				if (i - 1 >= 0)
					dp[i][j] += dp[i - 1][j];

				if (j - 1 >= 0)
					dp[i][j] += dp[i][j - 1];
			}
		}

		return dp[M - 1][N - 1];
	}
}
