class Solution {
    private boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U'; 
    }

    public boolean halvesAreAlike(String s) {
        int left = 0, right = 0;
        for (int i = 0; i < s.length()/2; i++) {
            if (isVowel(s.charAt(i))) left++;
            if (isVowel(s.charAt(s.length()-i-1))) right++; 
        }
        return left == right;
    }
}