// https://leetcode.com/problems/available-captures-for-rook/ 

class Solution {
	public int numRookCaptures(char[][] board) {
		int ri;
		int rj;
		int i;
		int j;
		int n;

		// find the rook
		ri = 0;
		rj = 0;
		while (board[ri][rj] != 'R') {
			rj++;
			if (rj >= board[ri].length) {
				ri++;
				rj = 0;
			}
		}

		// initially we've captured no pawns	
		n = 0;
	
		// go north
		for (i = ri; i >= 0 && board[i][rj] != 'p' && board[i][rj] != 'B'; i--);
		if (i >= 0 && board[i][rj] == 'p')
			n++;

		// go south
		for (i = ri; i < board.length && board[i][rj] != 'p' && board[i][rj] != 'B'; i++);
		if (i < board.length && board[i][rj] == 'p')
			n++;

		// go west
		for (j = rj; j >= 0 && board[ri][j] != 'p' && board[ri][j] != 'B'; j--);
		if (j >= 0 && board[ri][j] == 'p')
			n++;

		// go east
		for (j = rj; j < board[ri].length && board[ri][j] != 'p' && board[ri][j] != 'B'; j++);
		if (j < board[ri].length && board[ri][j] == 'p')
			n++;

		return n;
	}
}
