import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public List<Integer> solution(String s) {
        List<Integer> answer = new ArrayList<>();
        s = s.substring(2,s.length()-2);
        s = s.replace("},{"," ");
        String[] arr1 = s.split(" ");
        Arrays.sort(arr1, new Comparator<String>() {
            public int compare(String o1, String o2) {
                if (o1.length()>o2.length()){
                    return 1;
                }
                else{
                    return -1;
                }
            }
        });
        for(String str:arr1){
            String [] arr2 = str.split(",");
            for (int i = 0; i < arr2.length; i++) {
                int temp = Integer.parseInt(arr2[i]);
                if(!answer.contains(temp)){
                    answer.add(temp);
                }
            }
        }
        return answer;
    }
}