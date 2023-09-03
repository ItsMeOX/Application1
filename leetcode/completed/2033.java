public class 2033 {
    class Solution {
        public int minOperations(int[][] grid, int x) {
            int m = grid.length, n = grid[0].length;
            int[] flatten = new int[m*n];
    
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++ ) {
                    flatten[i*n+j] = grid[i][j];
                }
            }
    
            Arrays.sort(flatten);
            int target = flatten[flatten.length / 2];
    
            int res = 0;
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++ ) {
                    if (Math.abs(grid[i][j] - target) % x != 0) return -1;
                    res += Math.abs(grid[i][j] - target) / x;
                }
            }
    
            return res;
    
        }
    }
}
