class Solution {
    public String solution(String s) {
        s = s.toLowerCase();
        if(!Character.isDigit(s.charAt(0))){
            s=Character.toUpperCase(s.charAt(0)) + s.substring(1);
        }
        for (int i = 1; i < s.length(); i++) {
            if(Character.isSpaceChar(s.charAt(i))){
                continue;
            } else if(Character.isDigit(s.charAt(i))){
                continue;
            } else if(Character.isSpaceChar(s.charAt(i-1))){
                s= s.substring(0,i) + Character.toUpperCase(s.charAt(i)) + s.substring(i+1);
            }
        }
        return s;
    }
}