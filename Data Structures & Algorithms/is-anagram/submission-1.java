class Solution {
    public boolean isAnagram(String s, String t) {
        int length1 = s.length();
        int length2 = t.length();
        if (length1 != length2) return false;
        HashMap<Character, Integer> map = new HashMap();
        for(int idx=0; idx<length1; idx++){
            if(map.containsKey(s.charAt(idx))){
                map.put(s.charAt(idx), map.get(s.charAt(idx)) + 1);
            } else {
                map.put(s.charAt(idx), 1);
            }
        }
        for(int idx=0; idx<length2; idx++){
            if (map.containsKey(t.charAt(idx))){
                map.put(t.charAt(idx), map.get(t.charAt(idx)) - 1);
                if (map.get(t.charAt(idx)) < 0){
                    return false;
                }
            }
            else{
                return false;
            }
        }
        return true;
    }
}
