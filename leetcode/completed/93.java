public class 93 {
    class Solution {
        private void dfs(String s, ArrayList<String> res, int i, String cur_str, int dot_cnt) {
            if (dot_cnt > 4) return;
            if (i == s.length()) {
                if (dot_cnt == 4) res.add(cur_str.substring(0, cur_str.length()-1));
                return ;
            }
    
            if (s.charAt(i) == '0') {
                dfs(s, res, i+1, cur_str + '0' + '.', dot_cnt + 1);
                return ;
            }
    
            for (int delta = 1; delta < 4; delta++) {
                if (i+delta > s.length()) continue;
                String substr = s.substring(i, i+delta);
                if (Integer.parseInt(substr) > 255) continue;
                dfs(s, res, i+delta, cur_str + substr + '.', dot_cnt + 1);
            }
    
        }
    
        public List<String> restoreIpAddresses(String s) {
            ArrayList<String> res = new ArrayList<>();
            dfs(s, res, 0, "", 0);
            return res;
        }
    }
}
