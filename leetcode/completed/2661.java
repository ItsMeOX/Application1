// record the x, y position in a hashmap / array,
// then iterate through arr and check row[y] == col_len or col[x] == row_len,
// if true then return current index.

public class 2661 {
    class Solution {
        public int firstCompleteIndex(int[] arr, int[][] mat) {
            int m = mat.length, n = mat[0].length;
            int[] row = new int[m];
            int[] col = new int[n];
            int[][] position = new int[m*n+1][2];
    
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    position[mat[i][j]] = new int[]{i, j};
                }
            }
    
            for (int i = 0; i < arr.length; i++) {
                int[] pos = position[arr[i]];
                int r = pos[0], c = pos[1];
    
                if(++row[r] == n || ++col[c] == m) return i;
            }
    
            return -1;
    
        }
    }
}
