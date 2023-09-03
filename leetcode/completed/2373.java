public class 2373 {
    class Solution {
        public int[][] largestLocal(int[][] grid) {
            int n = grid.length;
            int[][] res = new int[n-2][n-2];
    
            for (int r = 1; r < n-1; r++) {
                for (int c = 1; c < n-1; c++) {
                    int t = 0;
                    for (int dc = -1; dc < 2; dc++) {
                        for (int dr = -1; dr < 2; dr++) {
                            t = Math.max(t, grid[r+dr][c+dc]);
                        }
                    }
                    res[r-1][c-1] = t;
                }
            } 
    
            return res;
        }
    }
}
