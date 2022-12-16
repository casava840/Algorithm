def solution(n,a,b):
    round = 1
    if a>b:
        a,b = b,a
    a,b = a-1,b-1
    if a+1 == b and b%2==1:
        return round
    while a+1 != b or b%2 != 1:
        a = a//2
        b = b//2
        round += 1
    return round