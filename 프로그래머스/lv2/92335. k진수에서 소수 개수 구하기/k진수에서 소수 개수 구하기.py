def solution(n, k):
    p = []
    converted = ""
    answer = 0
    if k == 10:
        p = str(n).split('0')
    else:
        while n:
            converted = str(n % k) + converted
            n = n // k
        p = converted.split('0')
    for i in p:
        flag = False
        if i == '':
            continue
        elif int(i) > 1:
            for j in range(2, int(int(i)**(1/2)) + 1):
                if int(i) % j == 0:
                    flag = True
                    break
            if flag == False:
                answer += 1
        else:
            continue
    
    return answer