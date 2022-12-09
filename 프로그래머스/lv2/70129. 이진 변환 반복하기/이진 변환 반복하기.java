class Solution {
    public int[] solution(String s) {
        
        return transformBinary(s,0,0);
    }
    private static int[] transformBinary(String s, int sum,int transformCount) {
        int zeroCount = 0;
        if(s.equals("1")) {
            return new int[] {transformCount,sum};
        }
        for (int i = 0; i < s.length(); i++) {
            if(s.charAt(i)=='0'){
                zeroCount++;
            }
        }
        sum += zeroCount;
        transformCount++;
        String newS = Integer.toBinaryString(s.length()-zeroCount);
        return transformBinary(newS,sum,transformCount);
    }
}