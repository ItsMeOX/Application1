public class 1584 {
    class Solution {

        public int minCostConnectPoints(int[][] points) {
            int res = 0;
            int edge = 0;
            PriorityQueue<int[]> q = new PriorityQueue<>(Comparator.comparingInt(pair -> pair[0]));
            int[] visited = new int[points.length];
            q.add(new int[]{0, 0});
    
            while (edge < points.length) {
                int[] pair = q.poll();
                int cost = pair[0], i = pair[1];
                if (visited[i] == 1) continue;
                res += cost;
                edge++;
                visited[i] = 1;
    
                for (int j = 0; j < points.length; j++) {
                    int new_cost = Math.abs(points[i][0]-points[j][0]) + Math.abs(points[i][1]-points[j][1]);
                    if (visited[j] == 0) q.add(new int[]{new_cost, j});
                }
    
            }
    
            return res;
        }
    }
}
