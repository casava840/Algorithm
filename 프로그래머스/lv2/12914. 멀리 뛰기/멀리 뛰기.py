import math
def solution(n):
    answer = 0
    for amount_of_2 in range(0,n//2+1):
        amount_of_1 = n - 2*amount_of_2
        sum = amount_of_1 + amount_of_2
        answer += math.comb(sum,amount_of_2)
    return answer%1234567