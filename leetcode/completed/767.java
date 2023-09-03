class Solution {
    public String reorganizeString(String s) {
        char[] res = s.toCharArray();
        int[] counter = new int[26];
        int max_freq = 0;
        char max_char = 0;
        int n = s.length();

        for (char c : res) {
            counter[c - 'a']++;
            if (counter[c - 'a'] > max_freq) {
                max_freq = counter[c - 'a'];
                max_char = c;
            }
        }

        if (max_freq > (n + 1) / 2) return "";

        int i = 0;

        while(max_freq-- > 0) {
            res[i] = max_char;
            i += 2;
        }
        counter[max_char - 'a'] = 0;

        for (int j = 0; j < 26; j++) {
            while (counter[j]-- > 0) {
                i = i >= n ? 1 : i;
                res[i] = (char)('a' + j);
                i += 2;
            }
        }

        return String.valueOf(res);

    }
}