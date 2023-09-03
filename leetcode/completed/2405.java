public class 2405 {
    class Solution {
        public int partitionString(String s) {
            int res = 1;
            HashSet<Character> seen = new HashSet<>();
    
            for (int i = 0; i < s.length(); i++) {
                if (seen.contains(s.charAt(i))) {
                    res++;
                    seen.clear();
                }
                seen.add(s.charAt(i));
            }
    
            return res;
        }
    }
}

class Solution {
    private void clear(int[] seen) {
        for (int i = 0; i < 26; i++) {
            seen[i] = 0;
        }
    }

    public int partitionString(String s) {
        int res = 1;
        int[] seen = new int[26];

        for (int i = 0; i < s.length(); i++) {
            if (seen[s.charAt(i)-'a'] == 1) {
                res++;
                clear(seen);
            }
            seen[s.charAt(i)-'a'] = 1;
        }

        return res;
    }
}