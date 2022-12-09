class Solution {
    boolean solution(String s) {
        int count= 0;
        boolean answer = true;
        for(int i=0; i<s.length(); i++){
            if(s.charAt(i)=='('){
                count++;
            }
            else{
                count--;
                if(count<0){
                    answer = false;
                    break;
                }
            }
        }
        if(count!=0){
            answer = false;
        }
        return answer;
    }
}