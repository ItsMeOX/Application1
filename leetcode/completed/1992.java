class Solution {
    class Pair {
        int r, c;

        public Pair(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }


    public int[][] findFarmland(int[][] land) {
        int m=land.length, n=land[0].length;
        List<int[]> res = new ArrayList<>();
        Deque<Pair> q = new ArrayDeque<>();
        Pair[] directions = {new Pair(0, 1), new Pair(1, 0)};

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (land[r][c] == 1) {
                    land[r][c] = -1;
                    int[] rect = {r, c, r, c};
                    q.add(new Pair(r, c));
                    while (q.size() > 0) {
                        Pair pair = q.removeFirst();
                        int rr = pair.r;
                        int cc = pair.c;
                        rect[2] = rr;
                        rect[3] = cc;
                        for (Pair direction : directions) {
                            int dr = direction.r;
                            int dc = direction.c;
                            if (rr + dr < m && cc + dc < n && land[rr+dr][cc+dc] == 1) {
                                land[rr+dr][cc+dc] = -1;
                                q.add(new Pair(rr+dr, cc+dc));
                            }
                        }
                    }
                    res.add(rect);
                }
            }
        }

        return res.toArray(new int[0][0]);

    }
}