class Solution {
    public String longestCommonPrefix(String[] strs) {
        Arrays.sort(strs);
        String firstWord = strs[0];
        String lastWord = strs[strs.length-1];
        int commonTill = 0;
        while(commonTill < (Math.min(firstWord.length(), lastWord.length()))){
            if (firstWord.charAt(commonTill) == lastWord.charAt(commonTill)){
                commonTill++;
            }
            else{
                return firstWord.substring(0, commonTill);
            }
        }
        return firstWord.substring(0, commonTill);
    }
}