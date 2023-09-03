public class 1410 {
    class Solution {
        public String entityParser(String text) {
            String[] key = new String[] {"&quot;", "&apos;", "&gt;", "&lt;", "&frasl;", "&amp;"};
            String[] value = new String[] {"\"", "'", ">", "<", "/", "&"};
    
            for (int i = 0; i < 6; i++) {
                text = text.replace(key[i], value[i]);
            }
    
            return text;
        }
    }
}
