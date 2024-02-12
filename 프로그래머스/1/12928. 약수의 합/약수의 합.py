def solution(n):
    i = 1
    lis = [0]
    while i <= n**0.5:
        if n%i == 0:
            lis.append(i)
            lis.append(n/i)
        if n/i == i:
            lis.pop(-1)
        i += 1
    return sum(lis)