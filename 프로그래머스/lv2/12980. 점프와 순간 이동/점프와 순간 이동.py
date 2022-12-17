def solution(n):
    consummed_battery = 0
    while n>0:
        if n % 2 == 1:
            n = (n-1)/2
            consummed_battery += 1
        else:
            n /= 2
    return consummed_battery