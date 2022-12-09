import java.util.*;

class Solution
{
    public int solution(int []A, int []B)
    {
        Arrays.sort(A);
        Arrays.sort(B);
        int LENGTH = A.length;
        int answer = 0;
        int i = 0;
        while(i<LENGTH){
            answer += A[i]*B[LENGTH-i-1];
            i++;
        }
        return answer;
    }
}